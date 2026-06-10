#!/bin/bash
# ============================================================
# RelicTrek Daily Blog Automation — One-Click Installer
# For: macOS with GitHub
# Repo: /Users/yanfeiliu/Documents/GitHub/relictrek.net
# ============================================================

set -e

REPO_DIR="/Users/yanfeiliu/Documents/GitHub/relictrek.net"
PLIST_NAME="net.relictrek.dailyblog.plist"
PLIST_SRC="$REPO_DIR/blog/$PLIST_NAME"
PLIST_DST="$HOME/Library/LaunchAgents/$PLIST_NAME"
SCRIPT_PATH="$REPO_DIR/blog/run_daily_blog.sh"

echo "============================================"
echo " RelicTrek Daily Blog Automation Setup"
echo "============================================"
echo ""

# 1. Check repo exists
if [ ! -d "$REPO_DIR" ]; then
    echo "ERROR: Repo not found at $REPO_DIR"
    echo "Please clone your GitHub repo first:"
    echo "  git clone https://github.com/YOUR_USERNAME/relictrek.net.git ~/Documents/GitHub/relictrek.net"
    exit 1
fi
echo "[1/5] Repo found: $REPO_DIR"

# 2. Check Python3
PYTHON_PATH=$(which python3 2>/dev/null || true)
if [ -z "$PYTHON_PATH" ]; then
    echo "ERROR: python3 not found. Install it first:"
    echo "  brew install python3"
    exit 1
fi
echo "[2/5] Python3 found: $PYTHON_PATH"

# 3. Make script executable
chmod +x "$SCRIPT_PATH"
echo "[3/5] Made run_daily_blog.sh executable"

# 4. Install plist
cp "$PLIST_SRC" "$PLIST_DST"
chmod 644 "$PLIST_DST"
echo "[4/5] Installed launchd plist to $PLIST_DST"

# 5. Load launchd
launchctl load "$PLIST_DST" 2>/dev/null || launchctl bootstrap gui/$(id -u) "$PLIST_DST" 2>/dev/null
echo "[5/5] Loaded launchd job"

echo ""
echo "============================================"
echo " Installation Complete!"
echo "============================================"
echo ""
echo "Schedule: Every day at 3:00 AM"
echo "Logs:     $REPO_DIR/blog/.auto_blog.log"
echo "          $REPO_DIR/blog/.launchd.out.log"
echo ""
echo "Test now: launchctl start net.relictrek.dailyblog"
echo "Verify:   launchctl list | grep relictrek"
echo "Logs:     tail -f $REPO_DIR/blog/.auto_blog.log"
echo ""
echo "GitHub Actions is also enabled as backup:"
echo "  .github/workflows/daily-blog.yml"
echo ""
