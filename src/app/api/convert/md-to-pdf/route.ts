import { NextRequest, NextResponse } from 'next/server';
import { exec } from 'child_process';
import { promisify } from 'util';
import fs from 'fs/promises';
import path from 'path';
import crypto from 'crypto';

const execPromise = promisify(exec);

export async function POST(request: NextRequest) {
  try {
    const { markdown, filename = 'document' } = await request.json();
    
    if (!markdown) {
      return NextResponse.json(
        { error: 'No markdown content provided' },
        { status: 400 }
      );
    }

    // Create temp directory if it doesn't exist
    const tempDir = path.join(process.cwd(), 'temp');
    await fs.mkdir(tempDir, { recursive: true });

    // Generate unique filenames
    const uniqueId = crypto.randomBytes(8).toString('hex');
    const mdFile = path.join(tempDir, `${uniqueId}.md`);
    const pdfFile = path.join(tempDir, `${uniqueId}.pdf`);

    try {
      // Write markdown to temp file
      await fs.writeFile(mdFile, markdown, 'utf-8');

      // Try Chrome renderer method (more reliable on Mac)
      const htmlFile = pdfFile.replace('.pdf', '.html');
      
      try {
        // Convert MD to HTML first
        await execPromise(`pandoc "${mdFile}" -o "${htmlFile}" --self-contained`);
        
        // Use Chrome to convert HTML to PDF
        await execPromise(`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --print-to-pdf="${pdfFile}" "${htmlFile}"`);
        
        // Clean up HTML file
        await fs.unlink(htmlFile).catch(() => {});
      } catch (pandocError) {
        // Fallback to simple pandoc if Chrome method fails
        await execPromise(`pandoc "${mdFile}" -o "${pdfFile}" 2>&1`);
      }

      // Read the PDF file
      const pdfBuffer = await fs.readFile(pdfFile);

      // Clean up temp files
      await fs.unlink(mdFile).catch(() => {});
      await fs.unlink(pdfFile).catch(() => {});

      // Return PDF as response: use Blob with Uint8Array to satisfy Web BodyInit
      const uint8 = new Uint8Array(pdfBuffer);
      const blob = new Blob([uint8], { type: 'application/pdf' });
      return new NextResponse(blob, {
        status: 200,
        headers: {
          'Content-Type': 'application/pdf',
          'Content-Disposition': `attachment; filename="${filename}.pdf"`,
        },
      });
    } catch (error) {
      // Clean up on error
      await fs.unlink(mdFile).catch(() => {});
      await fs.unlink(pdfFile).catch(() => {});
      
      throw error;
    }
  } catch (error) {
    console.error('PDF conversion error:', error);
    return NextResponse.json(
      { 
        error: 'Failed to convert markdown to PDF',
        details: error instanceof Error ? error.message : 'Unknown error'
      },
      { status: 500 }
    );
  }
}

// GET endpoint to check if service is available
export async function GET() {
  try {
    const { stdout } = await execPromise('pandoc --version');
    const version = stdout.split('\n')[0];
    
    return NextResponse.json({
      status: 'ready',
      pandoc: version,
      message: 'MD to PDF conversion service is available'
    });
  } catch (error) {
    return NextResponse.json({
      status: 'error',
      message: 'Pandoc not installed. Run: brew install pandoc'
    }, { status: 503 });
  }
}