# Development Server

Start the Next.js development server with Turbopack.

## Usage
```
/dev
```

## What this command does
1. Clears any stale .next cache if needed
2. Starts development server on port 3001
3. Enables hot module replacement
4. Shows build errors in browser

## Actual command
```bash
npm run dev
```

## Troubleshooting
- Port 3000 in use: Automatically uses 3001
- Build errors: Check TypeScript and ESLint
- Memory issues: Clear .next folder