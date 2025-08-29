#!/usr/bin/env node

/**
 * Claude Code Health Check Script
 * Verifies project setup and environment
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Colors for terminal output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  red: '\x1b[31m',
  cyan: '\x1b[36m',
  bold: '\x1b[1m'
};

// Icons
const icons = {
  success: '✅',
  warning: '⚠️',
  error: '❌',
  info: 'ℹ️'
};

class HealthCheck {
  constructor() {
    this.results = [];
    this.hasErrors = false;
    this.hasWarnings = false;
  }

  log(status, message, details = '') {
    const icon = status === 'success' ? icons.success :
                 status === 'warning' ? icons.warning :
                 status === 'error' ? icons.error : icons.info;
    
    const color = status === 'success' ? colors.green :
                  status === 'warning' ? colors.yellow :
                  status === 'error' ? colors.red : colors.cyan;
    
    console.log(`${icon} ${color}${message}${colors.reset} ${details}`);
    
    if (status === 'error') this.hasErrors = true;
    if (status === 'warning') this.hasWarnings = true;
    
    this.results.push({ status, message, details });
  }

  checkCommand(command, name) {
    try {
      const version = execSync(`${command} --version`, { encoding: 'utf8' }).trim();
      this.log('success', `${name}:`, version.split('\n')[0]);
      return true;
    } catch (error) {
      this.log('error', `${name}:`, 'Not found');
      return false;
    }
  }

  checkNodeVersion() {
    try {
      const version = process.version;
      const major = parseInt(version.split('.')[0].substring(1));
      if (major >= 18) {
        this.log('success', 'Node.js:', version);
      } else {
        this.log('warning', 'Node.js:', `${version} (recommend v18+)`);
      }
    } catch (error) {
      this.log('error', 'Node.js:', 'Unable to check version');
    }
  }

  checkProjectFiles() {
    const requiredFiles = [
      'package.json',
      'tsconfig.json',
      'next.config.ts',
      'postcss.config.mjs'
    ];

    console.log(`\n${colors.bold}📁 Project Files:${colors.reset}`);
    
    requiredFiles.forEach(file => {
      if (fs.existsSync(file)) {
        this.log('success', file, 'Found');
      } else {
        this.log('error', file, 'Missing');
      }
    });
  }

  checkClaudeSetup() {
    console.log(`\n${colors.bold}🤖 Claude Setup:${colors.reset}`);
    
    // Check .claude folder
    if (fs.existsSync('.claude')) {
      this.log('success', '.claude folder:', 'Configured');
      
      // Check agents
      const agentsDir = '.claude/agents';
      if (fs.existsSync(agentsDir)) {
        const agents = fs.readdirSync(agentsDir).filter(f => f.endsWith('.md'));
        this.log('success', 'Agents:', `${agents.length} found`);
      } else {
        this.log('warning', 'Agents:', 'Folder missing');
      }
      
      // Check commands
      const commandsDir = '.claude/commands';
      if (fs.existsSync(commandsDir)) {
        const commands = fs.readdirSync(commandsDir).filter(f => f.endsWith('.md'));
        this.log('success', 'Commands:', `${commands.length} found`);
      } else {
        this.log('warning', 'Commands:', 'Folder missing');
      }
      
      // Check settings
      if (fs.existsSync('.claude/settings.json')) {
        this.log('success', 'Settings:', 'Configured');
      } else {
        this.log('warning', 'Settings:', 'Not configured');
      }
    } else {
      this.log('warning', '.claude folder:', 'Not found');
    }

    // Check MCP
    if (fs.existsSync('.mcp.json')) {
      this.log('success', 'MCP config:', 'Found');
    } else {
      this.log('info', 'MCP config:', 'Not configured');
    }
  }

  checkPorts() {
    console.log(`\n${colors.bold}🌐 Port Status:${colors.reset}`);
    
    const ports = [3000, 3001, 3333];
    
    ports.forEach(port => {
      try {
        execSync(`lsof -i :${port}`, { encoding: 'utf8' });
        this.log('warning', `Port ${port}:`, 'In use');
      } catch (error) {
        this.log('success', `Port ${port}:`, 'Available');
      }
    });
  }

  checkTypeScript() {
    console.log(`\n${colors.bold}📝 TypeScript Status:${colors.reset}`);
    
    try {
      execSync('npx tsc --noEmit', { encoding: 'utf8' });
      this.log('success', 'TypeScript:', 'No errors');
    } catch (error) {
      const output = error.stdout || error.stderr || '';
      const errorCount = (output.match(/error TS/g) || []).length;
      if (errorCount > 0) {
        this.log('error', 'TypeScript:', `${errorCount} errors found`);
      } else {
        this.log('warning', 'TypeScript:', 'Check manually');
      }
    }
  }

  checkDependencies() {
    console.log(`\n${colors.bold}📦 Dependencies:${colors.reset}`);
    
    try {
      const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
      const deps = Object.keys(packageJson.dependencies || {}).length;
      const devDeps = Object.keys(packageJson.devDependencies || {}).length;
      
      this.log('success', 'Dependencies:', `${deps} production, ${devDeps} development`);
      
      // Check for common issues
      if (packageJson.dependencies && packageJson.dependencies['react']) {
        const reactVersion = packageJson.dependencies['react'];
        this.log('info', 'React:', reactVersion);
      }
      
      if (packageJson.dependencies && packageJson.dependencies['next']) {
        const nextVersion = packageJson.dependencies['next'];
        this.log('info', 'Next.js:', nextVersion);
      }
    } catch (error) {
      this.log('error', 'Dependencies:', 'Unable to check');
    }
  }

  checkBuildStatus() {
    console.log(`\n${colors.bold}🔨 Build Status:${colors.reset}`);
    
    if (fs.existsSync('.next')) {
      const stats = fs.statSync('.next');
      const age = Date.now() - stats.mtimeMs;
      const hours = Math.floor(age / (1000 * 60 * 60));
      
      if (hours < 24) {
        this.log('success', '.next folder:', `Built ${hours}h ago`);
      } else {
        this.log('warning', '.next folder:', `Built ${hours}h ago (may be stale)`);
      }
    } else {
      this.log('info', '.next folder:', 'Not built yet');
    }
  }

  async run() {
    console.log(`${colors.bold}${colors.cyan}🏥 Claude Code Health Check${colors.reset}`);
    console.log(`${colors.cyan}${'='.repeat(40)}${colors.reset}\n`);

    console.log(`${colors.bold}🖥️  Environment:${colors.reset}`);
    this.checkNodeVersion();
    this.checkCommand('npm', 'npm');
    this.checkCommand('git', 'Git');

    this.checkProjectFiles();
    this.checkClaudeSetup();
    this.checkDependencies();
    this.checkTypeScript();
    this.checkPorts();
    this.checkBuildStatus();

    // Summary
    console.log(`\n${colors.cyan}${'='.repeat(40)}${colors.reset}`);
    console.log(`${colors.bold}📊 Summary:${colors.reset}`);
    
    if (this.hasErrors) {
      console.log(`${colors.red}❌ Some issues need attention${colors.reset}`);
    } else if (this.hasWarnings) {
      console.log(`${colors.yellow}⚠️  Some warnings to review${colors.reset}`);
    } else {
      console.log(`${colors.green}✅ All checks passed!${colors.reset}`);
    }

    // Recommendations
    if (this.hasErrors || this.hasWarnings) {
      console.log(`\n${colors.bold}💡 Recommendations:${colors.reset}`);
      
      this.results.forEach(result => {
        if (result.status === 'error') {
          if (result.message.includes('TypeScript')) {
            console.log('• Run `npx tsc --noEmit` to see TypeScript errors');
          }
          if (result.message.includes('.claude')) {
            console.log('• Run `mkdir -p .claude/agents .claude/commands` to create Claude structure');
          }
        }
        if (result.status === 'warning') {
          if (result.message.includes('Port')) {
            console.log('• Check running processes with `lsof -i :PORT`');
          }
        }
      });
    }

    process.exit(this.hasErrors ? 1 : 0);
  }
}

// Run health check
const healthCheck = new HealthCheck();
healthCheck.run();