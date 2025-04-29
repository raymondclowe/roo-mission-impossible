# Astro MDX Integration Guide

## Overview
This guide demonstrates how to integrate MDX with Astro, enabling the use of React components within Markdown files.

## Prerequisites
1. Astro project set up with MDX integration
2. `@astrojs/mdx` package installed

## Step 1: Configure Astro for MDX
In your `astro.config.mjs`:
```javascript
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  integrations: [mdx()],
  // Other configurations...
});
```

## Step 2: Create MDX Pages
1. Create `.mdx` files in your `src/pages` directory
2. Use frontmatter for page metadata
3. Import and use Astro components directly in MDX files

Example (`src/pages/sample.mdx`):
```mdx
---
title: "MDX Demo Page"
---

import Hero from '../components/Hero.astro'
import Footer from '../components/Footer.astro'

<Hero title="Welcome to MDX Demo" image="/assets/background.svg" />

## Markdown Content

This is a markdown section with **bold text** and *italic text*.

<Footer />
```

## Step 3: Create Components for MDX
1. For Astro components (.astro), you can use them directly in MDX
2. For React components, ensure you have the necessary setup (not covered in this guide due to mode restrictions)

## Troubleshooting
1. If you add new MDX files, restart your Astro dev server
2. Ensure proper import paths for components
3. Check Astro documentation for latest MDX integration updates

## Example Use Cases
- Creating complex layouts with Markdown content
- Using interactive React components within Markdown
- Building documentation sites with rich content

## Best Practices
- Keep component imports at the top of MDX files
- Use frontmatter for page metadata
- Test new MDX files after server restart