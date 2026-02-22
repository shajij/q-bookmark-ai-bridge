# Q Book Marker Pro - AI Bridge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Native messaging bridge that enables AI features in the [Q Book Marker Pro](https://addons.mozilla.org/firefox/addon/q-bookmark-pro/) Firefox extension by connecting it to your local Ollama installation.

## What is this?

The Q Book Marker Pro Firefox extension has AI-powered features (bookmark summaries and AI search). However, Firefox extensions cannot directly connect to localhost services like Ollama. This bridge solves that problem by acting as a secure intermediary.

## Getting Started

**Prerequisites:**
- [Q Book Marker Pro](https://addons.mozilla.org/firefox/addon/q-bookmark-pro/) Firefox extension installed
- [Ollama](https://ollama.ai) installed on your computer
- Python 3.7+ (usually pre-installed on macOS/Linux)

**Quick Start:**
```bash
# Clone this repository
git clone https://github.com/shajij/q-bookmark-ai-bridge.git
cd q-bookmark-ai-bridge

# Run installer
./install.sh  # macOS/Linux
# or
install.bat   # Windows

# Follow the prompts and restart Firefox
```

## Features

- ✅ Connects Firefox extension to local Ollama
- ✅ Privacy-first: All processing happens on your machine
- ✅ Secure: Uses Firefox's Native Messaging API
- ✅ Cross-platform: Works on macOS, Windows, and Linux
- ✅ Simple installation

## Requirements

- **Python 3.7+** (usually pre-installed on macOS/Linux)
- **Ollama** installed and running ([ollama.ai](https://ollama.ai))
- **Q Book Marker** Firefox extension installed

## Installation

### macOS / Linux

1. Download and extract this package
2. Open Terminal in the extracted folder
3. Run the installer:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
4. When prompted, enter your extension ID (see below)
5. Restart Firefox

### Windows

1. Download and extract this package
2. Double-click `install.bat`
3. When prompted, enter your extension ID (see below)
4. Restart Firefox

### Finding Your Extension ID

1. Open Firefox
2. Go to `about:debugging`
3. Click "This Firefox" in the left sidebar
4. Find "Q Book Marker Pro" in the list
5. Copy the "Internal UUID" (should be: `qbookmark-pro@qbookpro.dev`)

## Usage

### 1. Start Ollama

Make sure Ollama is running:
```bash
ollama serve
```

### 2. Enable AI in Extension

1. Open Q Book Marker Manager (click extension icon → "Manage Bookmarks")
2. Go to Settings tab
3. You should see "✅ Bridge Installed"
4. Check "Enable AI Features"
5. Click "Save Settings"

### 3. Use AI Features

- **AI Summaries**: Click "AI Summary" button on any bookmark
- **AI Search**: Use natural language queries in search

## Troubleshooting

### Bridge shows as "Not Installed"

1. Make sure you ran the installer
2. Verify the extension ID is correct
3. Restart Firefox completely
4. Check manifest file exists:
   - **macOS**: `~/Library/Application Support/Mozilla/NativeMessagingHosts/com.qbookmark.aibridge.json`
   - **Linux**: `~/.mozilla/native-messaging-hosts/com.qbookmark.aibridge.json`
   - **Windows**: `%APPDATA%\Mozilla\NativeMessagingHosts\com.qbookmark.aibridge.json`

### "Cannot connect to Ollama"

1. Make sure Ollama is running: `ollama serve`
2. Test Ollama: `curl http://localhost:11434/api/tags`
3. Check Ollama is on default port 11434

### Python not found

- **macOS/Linux**: Install Python 3 from [python.org](https://python.org)
- **Windows**: Install Python 3 from [python.org](https://python.org) and check "Add to PATH"

### Permission denied (macOS/Linux)

```bash
chmod +x bridge.py
chmod +x install.sh
```

## How It Works

```
Firefox Extension → Native Messaging → Python Bridge → Ollama → AI Response
```

1. Extension sends AI request via Native Messaging API
2. Bridge receives request and forwards to Ollama
3. Ollama processes with local AI model
4. Bridge returns result to extension
5. Extension displays AI response

## Security

- ✅ All communication stays on your machine
- ✅ No data sent to external servers
- ✅ Bridge only accepts messages from your extension
- ✅ Uses Firefox's secure Native Messaging API

## Uninstall

### macOS / Linux
```bash
rm ~/Library/Application\ Support/Mozilla/NativeMessagingHosts/com.qbookmark.aibridge.json  # macOS
rm ~/.mozilla/native-messaging-hosts/com.qbookmark.aibridge.json  # Linux
```

### Windows
Delete: `%APPDATA%\Mozilla\NativeMessagingHosts\com.qbookmark.aibridge.json`

Then delete this folder.

## Support

- **Extension Issues**: Contact via Firefox Add-ons page
- **Bridge Issues**: [Open an issue](https://github.com/shajij/q-bookmark-ai-bridge/issues)
- **Email**: cndtownmgmt@gmail.com
- **Ollama Issues**: See [Ollama documentation](https://ollama.ai)

## Security Considerations

⚠️ **Important Security Notes:**

1. **Local Processing Only**: All AI processing happens on your computer via Ollama. No data is sent to external servers.

2. **Trusted Bookmarks**: The AI Bridge processes bookmark titles and URLs. Only use with bookmarks from trusted sources.

3. **Input Sanitization**: The bridge sanitizes all inputs to prevent prompt injection attacks. However, exercise caution with untrusted bookmarks.

4. **Localhost Only**: The bridge only connects to localhost (127.0.0.1:11434). It cannot access external networks.

5. **Open Source**: All code is open source and auditable. Review the code before installation if you have security concerns.

6. **No Credentials**: The bridge does not store or transmit any credentials, API keys, or personal information.

7. **Privacy**: No data collection, tracking, or analytics. Everything stays on your machine.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See [LICENSE](LICENSE) file for details

## Acknowledgments

- Built for [Q Book Marker Pro](https://addons.mozilla.org/firefox/addon/q-bookmark-pro/)
- Powered by [Ollama](https://ollama.ai)

---

**Note**: The Q Book Marker Pro extension works perfectly without this bridge. AI features are completely optional.
