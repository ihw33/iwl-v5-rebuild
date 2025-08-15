# Health Check

Verify your Claude Code setup and project configuration.

## Usage
```
/health
```

## What this command checks

### Environment
- Node.js version
- npm/yarn version
- TypeScript version
- Next.js version

### Project Setup
- .claude folder structure
- Agents availability
- Commands configuration
- MCP connections

### Development Status
- Port availability (3000, 3001, 3333)
- Build status
- TypeScript errors
- ESLint warnings

### Performance
- Memory usage
- Disk space
- CPU load
- Network connectivity

## Output Example
```
✅ Node.js: v24.4.1
✅ Next.js: 15.4.6
✅ TypeScript: No errors
⚠️ Port 3000: In use
✅ Port 3001: Available
✅ .claude: Configured
✅ Agents: 3 loaded
✅ Commands: 4 available
```

## Troubleshooting Commands
```bash
# Check Node version
node --version

# Check TypeScript
npx tsc --version

# Check ports
lsof -i :3000
lsof -i :3001

# Check disk space
df -h

# Check memory
top -l 1 | grep PhysMem
```