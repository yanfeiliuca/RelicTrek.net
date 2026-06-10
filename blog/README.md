# RelicTrek Daily Blog System

## Overview

Automated daily blog generation system that creates unique blog posts about
RelicTrek's game items every day at 3:00 AM.

## Architecture

```
relictrek/
├── blog/
│   ├── index.html              # Blog homepage (EN)
│   ├── zh/index.html           # Blog homepage (ZH)
│   ├── 2026-06-04.html         # Individual blog posts (EN)
│   ├── zh/2026-06-04.html      # Individual blog posts (ZH)
│   ├── generate_daily_blog.py  # Blog generator script
│   ├── setup_cron.sh           # Cron/scheduler installer
│   ├── .blog_database.json     # Blog history database
│   └── .blog_cron.log          # Execution log
```

## How It Works

1. **Random Selection**: Picks a game item that hasn't been blogged about yet
2. **Content Generation**: Creates a blog post with community-style content
3. **Dual Language**: Generates both English and Chinese versions
4. **Auto-Publish**: Writes to blog/ directory and updates index pages
5. **Git Push**: Commits and pushes to relictrek.net (optional)

## Setup Instructions

### Step 1: Install Python 3
Ensure Python 3 is installed on your system.

### Step 2: Run the Setup Script

```bash
cd relictrek/blog
bash setup_cron.sh
```

This will:
- Detect your OS (Windows/macOS/Linux)
- Install the appropriate daily scheduler
- Set up logging

### Step 3: Test Manually

```bash
cd relictrek/blog
python generate_daily_blog.py
```

This generates today's blog post immediately.

### Step 4: Commit and Push

```bash
cd relictrek
git add blog/
git commit -m "Add daily blog system"
git push origin main
```

## Manual Commands

```bash
# Generate today's blog
python blog/generate_daily_blog.py

# Force regenerate (overwrite existing)
python blog/generate_daily_blog.py --force

# List all items and blog status
python blog/generate_daily_blog.py --list
```

## Daily Workflow (Automatic)

At 3:00 AM every day:
1. Script runs automatically
2. Picks a random unblogged item
3. Generates EN + ZH blog posts
4. Updates blog index pages
5. Commits and pushes (if git repo)

## Customization

To modify blog content style, edit `generate_blog_content()` function
in `generate_daily_blog.py`.

To change schedule time, edit `setup_cron.sh` and re-run.
