#!/bin/bash
# Q Bookmark AI Bridge Installer for macOS/Linux

set -e

echo "🤖 Q Bookmark AI Bridge Installer"
echo "=================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BRIDGE_SCRIPT="$SCRIPT_DIR/bridge.py"

# Make bridge executable
chmod +x "$BRIDGE_SCRIPT"

# Detect OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    MANIFEST_DIR="$HOME/Library/Application Support/Mozilla/NativeMessagingHosts"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    MANIFEST_DIR="$HOME/.mozilla/native-messaging-hosts"
else
    echo "❌ Unsupported OS: $OSTYPE"
    exit 1
fi

# Create manifest directory
mkdir -p "$MANIFEST_DIR"

# Get extension ID
echo ""
echo "📝 Enter your Q Bookmark extension ID:"
echo "(Find it in Firefox: about:debugging -> This Firefox -> Q Book Marker)"
read -p "Extension ID: " EXTENSION_ID

if [ -z "$EXTENSION_ID" ]; then
    echo "❌ Extension ID is required"
    exit 1
fi

# Create manifest
MANIFEST_FILE="$MANIFEST_DIR/com.qbookmark.aibridge.json"
cat > "$MANIFEST_FILE" << EOF
{
  "name": "com.qbookmark.aibridge",
  "description": "Q Bookmark AI Bridge",
  "path": "$BRIDGE_SCRIPT",
  "type": "stdio",
  "allowed_extensions": ["$EXTENSION_ID"]
}
EOF

echo ""
echo "✅ Bridge installed successfully!"
echo ""
echo "📍 Manifest location: $MANIFEST_FILE"
echo "📍 Bridge script: $BRIDGE_SCRIPT"
echo ""
echo "🔄 Next steps:"
echo "1. Make sure Ollama is running (ollama serve)"
echo "2. Restart Firefox"
echo "3. Open Q Bookmark Manager -> Settings"
echo "4. Enable AI features"
echo ""
echo "✨ Done!"
