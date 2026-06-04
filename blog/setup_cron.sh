#!/bin/bash
# RelicTrek Daily Blog Cron Setup
# Run this script to install the daily blog generation task
# Usage: bash setup_cron.sh

# Get the absolute path to the blog directory
BLOG_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$BLOG_DIR")"
PYTHON="$(which python3)"

if [ -z "$PYTHON" ]; then
    PYTHON="$(which python)"
fi

if [ -z "$PYTHON" ]; then
    echo "ERROR: Python 3 is required but not found."
    echo "Please install Python 3 first: https://python.org/downloads"
    exit 1
fi

echo "Setting up RelicTrek daily blog cron job..."
echo "  Blog directory: $BLOG_DIR"
echo "  Repository: $REPO_DIR"
echo "  Python: $PYTHON"

# Create catch-up script (runs on boot if a blog was missed)
CATCHUP="$BLOG_DIR/catch_up.sh"
cat > "$CATCHUP" << 'EOF'
#!/bin/bash
# Blog Catch-Up: Generate missed blog posts
BLOG_DIR="__BLOG_DIR__"
PYTHON="__PYTHON__"
LOG_FILE="$BLOG_DIR/.blog_catchup.log"

exec >> "$LOG_FILE" 2>&1
echo "Catch-up check: $(date)"

cd "$BLOG_DIR"

# Load last post date from database
DB_FILE="$BLOG_DIR/.blog_database.json"
if [ -f "$DB_FILE" ]; then
    LAST_DATE=$(python3 -c "import json; d=json.load(open('$DB_FILE')); print(d.get('last_post_date',''))" 2>/dev/null)
    TODAY=$(date +%Y-%m-%d)
    
    if [ -n "$LAST_DATE" ] && [ "$LAST_DATE" != "$TODAY" ] && [ "$LAST_DATE" != "" ]; then
        # Check if yesterday's blog exists
        YESTERDAY=$(date -d "yesterday" +%Y-%m-%d 2>/dev/null || date -v-1d +%Y-%m-%d 2>/dev/null)
        if [ "$LAST_DATE" = "$YESTERDAY" ] || [ "$LAST_DATE" \< "$TODAY" ]; then
            echo "Missed blog detected. Last: $LAST_DATE, Today: $TODAY"
            echo "Generating catch-up blog..."
            $PYTHON generate_daily_blog.py --force
            
            # Git push
            cd "__REPO_DIR__"
            if [ -d .git ] && git diff --quiet HEAD -- blog/ 2>/dev/null; then
                git add blog/
                git commit -m "Catch-up blog: $(date +%Y-%m-%d)"
                git push origin main
            fi
        fi
    fi
fi
echo "Catch-up check done: $(date)"
echo ""
EOF

sed -i "s|__BLOG_DIR__|$BLOG_DIR|g" "$CATCHUP"
sed -i "s|__REPO_DIR__|$REPO_DIR|g" "$CATCHUP"
sed -i "s|__PYTHON__|$PYTHON|g" "$CATCHUP"
chmod +x "$CATCHUP"

echo "Created catch-up script: $CATCHUP"

# Create a wrapper script that generates blog + commits + pushes
WRAPPER="$BLOG_DIR/daily_blog_wrapper.sh"
cat > "$WRAPPER" << 'EOF'
#!/bin/bash
# Daily Blog Auto-Generation & Push Wrapper
BLOG_DIR="__BLOG_DIR__"
REPO_DIR="__REPO_DIR__"
PYTHON="__PYTHON__"
LOG_FILE="$BLOG_DIR/.blog_cron.log"

exec >> "$LOG_FILE" 2>&1
echo "========================================"
echo "Blog generation started: $(date)"
echo "========================================"

# Step 1: Generate blog
cd "$BLOG_DIR"
$PYTHON generate_daily_blog.py

echo "Step 1: Blog generation complete"

# Step 2: Commit and push (if git repo exists)
if [ -d "$REPO_DIR/.git" ]; then
    cd "$REPO_DIR"
    
    # Check if there are changes
    if ! git diff --quiet HEAD -- blog/ 2>/dev/null; then
        echo "Step 2: Committing changes..."
        git add blog/
        git commit -m "Daily blog: $(date +%Y-%m-%d)"
        git push origin main
        echo "Step 3: Pushed to remote"
    else
        echo "Step 2: No changes to commit"
    fi
else
    echo "Step 2: Not a git repo, skipping push"
fi

echo "Blog generation finished: $(date)"
echo ""
EOF

# Replace placeholders in wrapper
sed -i "s|__BLOG_DIR__|$BLOG_DIR|g" "$WRAPPER"
sed -i "s|__REPO_DIR__|$REPO_DIR|g" "$WRAPPER"
sed -i "s|__PYTHON__|$PYTHON|g" "$WRAPPER"
chmod +x "$WRAPPER"

echo ""
echo "Created wrapper script: $WRAPPER"
echo ""

# Check OS and set up cron
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    echo "=== Windows Task Scheduler Setup ==="
    echo "Since you're on Windows, please set up Task Scheduler manually:"
    echo ""
    echo "=== TASK 1: Daily 3:00 AM Blog ==="
    echo "1. Open Task Scheduler (Win+R → taskschd.msc)"
    echo "2. Click 'Create Basic Task'"
    echo "3. Name: RelicTrek Daily Blog"
    echo "4. Trigger: Daily at 3:00 AM"
    echo "5. Action: Start a program"
    echo "6. Program: $PYTHON"
    echo "7. Arguments: $BLOG_DIR/generate_daily_blog.py"
    echo "8. Working directory: $BLOG_DIR"
    echo "9. Click Finish"
    echo ""
    echo "=== TASK 2: Boot Catch-Up (if missed) ==="
    echo "1. Create another task named: RelicTrek Blog Catch-Up"
    echo "2. Trigger: At startup (delay 2 minutes)"
    echo "3. Action: Start a program"
    echo "4. Program: $PYTHON"
    echo "5. Arguments: $BLOG_DIR/catch_up.sh"
    echo "6. Working directory: $BLOG_DIR"
    echo ""
    echo "Or run this PowerShell command as Administrator:"
    echo ""
    cat << POWERSHELL
\$Action = New-ScheduledTaskAction -Execute "$PYTHON" -Argument "$BLOG_DIR/generate_daily_blog.py" -WorkingDirectory "$BLOG_DIR"
\$Trigger = New-ScheduledTaskTrigger -Daily -At 3:00AM
\$Settings = New-ScheduledTaskSettingsSet
Register-ScheduledTask -TaskName "RelicTrek Daily Blog" -Action \$Action -Trigger \$Trigger -Settings \$Settings
POWERSHELL
    echo ""

elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS - use launchd
    PLIST="$HOME/Library/LaunchAgents/com.relictrek.dailyblog.plist"
    cat > "$PLIST" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.relictrek.dailyblog</string>
    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON</string>
        <string>$BLOG_DIR/generate_daily_blog.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>$BLOG_DIR</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>3</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$BLOG_DIR/.blog_cron.log</string>
    <key>StandardErrorPath</key>
    <string>$BLOG_DIR/.blog_cron.log</string>
</dict>
</plist>
EOF
    launchctl load "$PLIST" 2>/dev/null
    echo "✅ macOS launchd task installed: $PLIST"
    echo "   Runs daily at 3:00 AM"
    echo ""

else
    # Linux - use cron
    CRON_ENTRY="0 3 * * * $WRAPPER >> $BLOG_DIR/.blog_cron.log 2>&1"
    
    # Check if already installed
    if crontab -l 2>/dev/null | grep -q "relictrek"; then
        echo "Cron job already exists. Updating..."
        crontab -l 2>/dev/null | grep -v "relictrek" | crontab -
    fi
    
    # Install new cron job
    (crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -
    echo "✅ Linux cron job installed!"
    echo "   Runs daily at 3:00 AM"
    echo "   Cron entry: $CRON_ENTRY"
    echo ""
fi

echo "========================================"
echo "Setup complete!"
echo "========================================"
echo ""
echo "Blog database: $BLO