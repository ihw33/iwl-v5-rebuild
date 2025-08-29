# Clean Build Files

Remove build artifacts and cache files to resolve issues.

## Usage
```
/clean
```

## What this command does
1. Removes .next build folder
2. Clears node_modules/.cache
3. Removes TypeScript build info
4. Cleans npm cache if needed

## Commands executed
```bash
rm -rf .next
rm -rf node_modules/.cache
rm -f tsconfig.tsbuildinfo
```

## When to use
- Build errors persist
- Strange caching issues
- Before production build
- After major dependency updates