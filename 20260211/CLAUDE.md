# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains static HTML stock market reports with interactive data visualization. The reports are standalone HTML files that use CDN-hosted libraries (Tailwind CSS, Chart.js) and do not require a build process.

## File Structure

- `stock_report.html` - A股（中国）市场行情报告，包含人工智能、半导体、科创50、中证500、恒生科技等板块数据
- `us_stock_report.html` - 美股市场行情报告，包含纳斯达克、标普500、道琼斯三大指数及美股七巨头数据
- `ftp_server.py` - 简单的Python FTP服务器脚本（位于父目录）

## Development Server

To view the reports locally:

```bash
# Start HTTP server in the current directory
python3 -m http.server 8080
```

Then open:
- A股报告: http://localhost:8080/stock_report.html
- 美股报告: http://localhost:8080/us_stock_report.html

## Technical Stack

- **Tailwind CSS** (via CDN) - Utility-first CSS framework
- **Chart.js** (via CDN) - Interactive charts for market data visualization
- **Google Fonts** - Noto Sans SC for Chinese text rendering
- **Vanilla JavaScript** - No build tools or frameworks required

## Design System

### Color Scheme
- **Red** (`#ff6b6b`, `#ef4444`) - Indicates price increase (A股/港股惯例)
- **Green** (`#4ecdc4`, `#22c55e`) - Indicates price decrease (A股/港股惯例)
- **Gradient Headers** - Purple-to-pink for A股 report, Blue-to-cyan for 美股 report

### UI Components
- `.glass-effect` - Glassmorphism card style with backdrop blur
- `.card-hover` - Hover animation with elevation shadow
- `.animate-fade-in` - Staggered entrance animations
- Theme toggle button (fixed position, top-right)

### Dark Mode
Both reports support dark mode:
- Toggle via fixed button in top-right corner
- Preference saved to localStorage
- Chart.js charts dynamically update colors when theme changes

## Stock Report Conventions

### A股 Report (`stock_report.html`)
- Tracks: 上证指数, 深证成指, 创业板指, 科创50, 恒生指数, 恒生科技
- Sectors: 人工智能, 半导体
- Color coding follows Chinese market conventions (red=up, green=down)

### 美股 Report (`us_stock_report.html`)
- Indices: 道琼斯工业指数, 标普500, 纳斯达克
- Magnificent Seven: AAPL, MSFT, GOOGL, AMZN, NVDA, META, TSLA
- Includes 中概股 section
- Each stock has brand-colored icon

## Data Sources

Reports are populated with data from:
- 财联社, 证券时报, 新浪财经, 同花顺, 东方财富 (A股)
- Investing.com, Yahoo Finance, 富途资讯 (美股)

## Notes

- These are static snapshot reports for specific dates (2026-02-11)
- Data is hardcoded in HTML; no API integration
- Reports are self-contained single files with no external dependencies beyond CDNs
