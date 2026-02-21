#!/bin/bash
# Auto-update bridge manifest with current extension ID

echo "Enter the current extension ID from about:debugging:"
read EXTENSION_ID

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BRIDGE_SCRIPT="$SCRIPT_DIR/bridge.py"

cat > "$HOME/Library/Application Support/Mozilla/NativeMessagingHosts/com.qbookmark.aibridge.json" << EOF
{
  "name": "com.qbookmark.aibridge",
  "description": "Q Bookmark AI Bridge",
  "path": "$BRIDGE_SCRIPT",
  "type": "stdio",
  "allowed_extensions": ["$EXTENSION_ID"]
}
EOF

echo "✅ Updated! Restart Firefox."
