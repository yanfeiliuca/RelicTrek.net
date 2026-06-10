#!/bin/bash
# ============================================================
# RelicTrek Daily Blog Auto-Generator
# Runs every day at 3:00 AM via launchd
# ============================================================

REPO_DIR="/Users/yanfeiliu/Documents/GitHub/relictrek.net"
BLOG_DIR="$REPO_DIR/blog"
LOG_FILE="$BLOG_DIR/.auto_blog.log"
DATE=$(date '+%Y-%m-%d')
TIME=$(date '+%H:%M:%S')

# Detect Python3 path
PYTHON_PATH=$(which python3 2>/dev/null || echo "/usr/local/bin/python3")

echo "[$DATE $TIME] ==========================================" >> "$LOG_FILE"
echo "[$DATE $TIME] Starting daily blog generation..." >> "$LOG_FILE"
echo "[$DATE $TIME] Python: $PYTHON_PATH" >> "$LOG_FILE"

# Step 1: Generate blog
cd "$BLOG_DIR" || {
    echo "[$DATE $TIME] ERROR: Cannot cd to $BLOG_DIR" >> "$LOG_FILE"
    exit 1
}

$PYTHON_PATH generate_daily_blog.py >> "$LOG_FILE" 2>&1
GEN_STATUS=$?

if [ $GEN_STATUS -ne 0 ]; then
    echo "[$DATE $TIME] ERROR: Blog generation failed (exit $GEN_STATUS)" >> "$LOG_FILE"
    exit 1
fi

echo "[$DATE $TIME] Blog generated successfully" >> "$LOG_FILE"

# Step 2: Check if there are changes to commit
cd "$REPO_DIR" || exit 1

if git diff --quiet && git diff --staged --quiet; then
    echo "[$DATE $TIME] No changes to commit (blog may already exist)" >> "$LOG_FILE"
    echo "[$DATE $TIME] Done." >> "$LOG_FILE"
    exit 0
fi

# Step 3: Git commit and push
git add -A >> "$LOG_FILE" 2>&1
git commit -m "auto: daily blog $DATE" >> "$LOG_FILE" 2>&1
GIT_COMMIT_STATUS=$?

if [ $GIT_COMMIT_STATUS -ne 0 ]; then
    echo "[$DATE $TIME] ERROR: Git commit failed" >> "$LOG_FILE"
    exit 1
fi

git push origin main >> "$LOG_FILE" 2>&1
GIT_PUSH_STATUS=$?

if [ $GIT_PUSH_STATUS -eq 0 ]; then
    echo "[$DATE $TIME] SUCCESS: Blog pushed to GitHub" >> "$LOG_FILE"
else
    echo "[$DATE $TIME] ERROR: Git push failed (exit $GIT_PUSH_STATUS)" >> "$LOG_FILE"
fi

echo "[$DATE $TIME] Done." >> "$LOG_FILE"
