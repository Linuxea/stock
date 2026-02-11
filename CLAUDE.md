# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a static HTML repository for Chinese A-share and US stock market reports. Reports are self-contained HTML files with interactive data visualization using Chart.js.

## Development Server

To view reports locally:

```bash
cd 20260211
python3 -m http.server 8080
# Open http://localhost:8080/stock_report.html or us_stock_report.html
```

## Architecture

- **Static HTML files** - No build system, no package management
- **Tailwind CSS** - Loaded via CDN (tailwindcss.com)
- **Chart.js** - Loaded via CDN for data visualization
- **Google Fonts** - Noto Sans SC for Chinese text rendering

## File Structure

```
20260211/
├── stock_report.html      # A-share (China) market report
└── us_stock_report.html   # US stock market report
```

## Design System

### Color Conventions
- **A-share/China markets**: Red = Up, Green = Down
- **US markets**: Standard coloring (Green = Up, Red = Down)

### CSS Classes
- `.gradient-bg` - Header gradient backgrounds
- `.glass-effect` - Card backgrounds with backdrop blur
- `.card-hover` - Hover animations (translateY + shadow)
- `.animate-fade-in` - Entry animations with staggered delays

### Dark Mode
- Toggle button fixed at top-right
- Theme saved to localStorage
- Charts dynamically update colors on theme switch
- CSS: `html.dark` prefix for dark mode styles

## Creating New Reports

When creating new daily reports:

1. Create a new folder with date format `YYYYMMDD/`
2. Copy template from previous report or create new HTML
3. Update:
   - Title tag
   - Date in header
   - Market data (hardcoded)
   - Chart data arrays
4. Maintain consistent styling with existing reports

## Data Sources

Reports cite: 财联社, 证券时报, 新浪财经, 同花顺, 东方财富, Investing.com, Yahoo Finance, 富途资讯
