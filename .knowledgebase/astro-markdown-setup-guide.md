# Astro Markdown Integration Knowledge Base

## Overview
This guide documents the complete process of setting up an Astro project with Markdown support, including solutions to common compatibility issues encountered during configuration.

---

## 🧩 Requirements
- Node.js v18.17.1+ (or v20.3.0+/v22.0.0+)
- npm v9.6.5+
- Basic understanding of Astro framework

---

## 🛠️ Setup Process

### 1. Project Structure
```
astro-demo/
├── src/
│   ├── pages/          # Markdown and Astro pages
│   ├── layouts/        # Layout components
├── astro.config.mjs    # Astro configuration
├── package.json        # Project dependencies
```

### 2. Initial Setup
```bash
# Create project directory
mkdir astro-demo
cd astro-demo

# Initialize project
npm init -y
```

### 3. Dependency Installation
```bash
# Install compatible versions with legacy peer deps
npm install --legacy-peer-deps \
  astro@^4.3.0 \
  @astrojs/mdx@^2.3.1
```

### 4. Configuration
**astro.config.mjs**
```javascript
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  integrations: [mdx()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark'  // Syntax highlighting theme
    }
  }
});
```

**package.json**
```json
{
  "type": "module",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  }
}
```

---

## 🚨 Common Issues & Solutions

### Issue 1: Module Not Found
**Error:** `Cannot find module '@astrojs/mdx'`  
**Solution:**  
```bash
npm install --legacy-peer-deps
```

### Issue 2: Version Conflict
**Error:** `peer astro@"^4.0.0" from @astrojs/mdx@2.3.1`  
**Solution:**  
Downgrade Astro to v4.3.0:
```bash
npm install astro@^4.3.0
```

### Issue 3: ESM Configuration
**Error:** `Cannot use import statement outside a module`  
**Solution:**  
Add `"type": "module"` to package.json

---

## 🧪 Verification
1. Start development server:
```bash
npm run dev
```

2. Access at: http://localhost:4322

3. Create test pages:
```markdown
<!-- src/pages/test.md -->
---
title: Test Page
---

# This is a markdown page
```

---

## 📌 Key Takeaways
1. Use `--legacy-peer-deps` for version conflicts
2. Astro v4.x is required for MDX integration
3. Always set `"type": "module"` for ESM projects
4. Port 4322 is used when port 3000 is unavailable
5. Clean installation order: dependencies first, config second

---

## 📚 References
- [Astro MDX Documentation](https://docs.astro.build/en/guides/integrations-guide/mdx/)
- [Node.js ESM Documentation](https://nodejs.org/docs/latest-v18.x/doc/api/esm.html)
- [npm Peer Dependencies Guide](https://docs.npmjs.com/cli/v9/commands/npm-install)