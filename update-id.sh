#!/bin/bash
# Auto-update bridge manifest with current extension ID

echo "Enter the current extension ID from about:debugging:"
read EXTENSION_ID

cat > "$HOME/Library/Application Support/Mozilla/NativeMessagingHosts/com.qbookmark.aibridge.json" << EOF
{
  "name": "com.qbookmark.aibridge",
  "description": "Q Bookmark AI Bridge",
  "path": "/Users/johshaji/q-bookmark-ai-bridge/bridge.py",
  "type": "stdio",
  "allowed_extensions": ["$EXTENSION_ID"]
}
EOF

echo "✅ Updated! Restart Firefox."
