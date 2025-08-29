# Test Runner

Run tests for the IWL v5.0 project.

## Usage
```
/test
/test [specific-file]
/test --watch
/test --coverage
```

## Test Commands

### Unit Tests
```bash
npm test
```

### Type Checking
```bash
npx tsc --noEmit
```

### Linting
```bash
npx eslint src --ext ts,tsx
```

### Build Test
```bash
npm run build
```

## Coverage Report
```bash
npm test -- --coverage
```

Always run tests before committing changes.