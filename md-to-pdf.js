#!/usr/bin/env node

/**
 * Markdown to PDF Converter
 * Supports multiple conversion methods
 */

const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');
const util = require('util');
const execPromise = util.promisify(exec);

class MDtoPDFConverter {
  constructor() {
    this.pandocPath = '/opt/homebrew/bin/pandoc';
  }

  async checkPandoc() {
    try {
      const { stdout } = await execPromise(`${this.pandocPath} --version`);
      console.log('✅ Pandoc found:', stdout.split('\n')[0]);
      return true;
    } catch (error) {
      console.error('❌ Pandoc not found. Install with: brew install pandoc');
      return false;
    }
  }

  async convert(inputFile, outputFile = null) {
    // Check if input file exists
    if (!fs.existsSync(inputFile)) {
      throw new Error(`Input file not found: ${inputFile}`);
    }

    // Generate output filename if not provided
    if (!outputFile) {
      const dir = path.dirname(inputFile);
      const basename = path.basename(inputFile, path.extname(inputFile));
      outputFile = path.join(dir, `${basename}.pdf`);
    }

    console.log(`📄 Converting: ${inputFile}`);
    console.log(`📑 Output: ${outputFile}`);

    // Pandoc command with nice styling
    const command = `${this.pandocPath} "${inputFile}" \
      -o "${outputFile}" \
      --pdf-engine=xelatex \
      --highlight-style=tango \
      --toc \
      --toc-depth=3 \
      -V geometry:margin=1in \
      -V fontsize=11pt \
      -V linkcolor=blue \
      -V urlcolor=blue \
      -V toccolor=gray \
      --metadata title="Converted from Markdown" \
      2>&1`;

    try {
      const { stdout, stderr } = await execPromise(command);
      if (stderr) {
        console.warn('⚠️ Warnings:', stderr);
      }
      console.log('✅ PDF created successfully!');
      return outputFile;
    } catch (error) {
      // Fallback to simpler conversion if xelatex fails
      console.log('📝 Trying simpler conversion method...');
      const simpleCommand = `${this.pandocPath} "${inputFile}" -o "${outputFile}" 2>&1`;
      
      try {
        await execPromise(simpleCommand);
        console.log('✅ PDF created successfully (simple mode)!');
        return outputFile;
      } catch (fallbackError) {
        throw new Error(`Conversion failed: ${fallbackError.message}`);
      }
    }
  }

  async convertWithHTML(inputFile, outputFile = null) {
    // Alternative method using HTML intermediate
    if (!outputFile) {
      const dir = path.dirname(inputFile);
      const basename = path.basename(inputFile, path.extname(inputFile));
      outputFile = path.join(dir, `${basename}.pdf`);
    }

    const tempHtml = outputFile.replace('.pdf', '.html');

    try {
      // First convert to HTML
      await execPromise(`${this.pandocPath} "${inputFile}" -o "${tempHtml}" --self-contained`);
      
      // Then use Chrome to convert HTML to PDF
      const chromeCommand = `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
        --headless \
        --disable-gpu \
        --print-to-pdf="${outputFile}" \
        "${tempHtml}"`;
      
      await execPromise(chromeCommand);
      
      // Clean up temp HTML
      fs.unlinkSync(tempHtml);
      
      console.log('✅ PDF created using Chrome renderer!');
      return outputFile;
    } catch (error) {
      throw new Error(`HTML conversion failed: ${error.message}`);
    }
  }

  async batchConvert(pattern) {
    const glob = require('glob');
    const files = glob.sync(pattern);
    
    if (files.length === 0) {
      console.log('No files found matching pattern:', pattern);
      return;
    }

    console.log(`Found ${files.length} files to convert`);
    
    for (const file of files) {
      try {
        await this.convert(file);
      } catch (error) {
        console.error(`Failed to convert ${file}:`, error.message);
      }
    }
  }
}

// CLI usage
async function main() {
  const converter = new MDtoPDFConverter();
  
  // Check if pandoc is available
  const hasPandoc = await converter.checkPandoc();
  if (!hasPandoc) {
    process.exit(1);
  }

  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log(`
📚 Markdown to PDF Converter

Usage:
  node md-to-pdf.js <input.md> [output.pdf]
  node md-to-pdf.js --batch "*.md"
  node md-to-pdf.js --chrome <input.md>

Examples:
  node md-to-pdf.js README.md
  node md-to-pdf.js README.md docs/readme.pdf
  node md-to-pdf.js --batch "docs/*.md"
  node md-to-pdf.js --chrome README.md

Options:
  --batch    Convert multiple files
  --chrome   Use Chrome for rendering (better for complex layouts)
    `);
    return;
  }

  try {
    if (args[0] === '--batch') {
      await converter.batchConvert(args[1] || '*.md');
    } else if (args[0] === '--chrome') {
      await converter.convertWithHTML(args[1], args[2]);
    } else {
      await converter.convert(args[0], args[1]);
    }
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

// Export for use as module
module.exports = MDtoPDFConverter;

// Run if called directly
if (require.main === module) {
  main();
}