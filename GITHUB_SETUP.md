# GitHub Repository Setup Instructions

## Create GitHub Repository for AI Bridge

### 1. Create Repository on GitHub

1. Go to https://github.com/new
2. **Repository name:** `q-bookmark-ai-bridge`
3. **Description:** `AI Bridge for Q Book Marker Pro Firefox extension - enables local AI features via Ollama`
4. **Visibility:** Public
5. **Initialize:** Do NOT initialize with README (we already have one)
6. Click "Create repository"

### 2. Push Code to GitHub

```bash
cd /Users/johshaji/q-bookmark-ai-bridge

# Add GitHub remote (replace 'yourusername' with your GitHub username)
git remote add origin https://github.com/yourusername/q-bookmark-ai-bridge.git

# Push code
git branch -M main
git push -u origin main
```

### 3. Create Release

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. **Tag:** `v1.0.0`
4. **Title:** `Q Bookmark AI Bridge v1.0.0`
5. **Description:**
```markdown
# Q Bookmark AI Bridge v1.0.0

First release of the AI Bridge for Q Book Marker Pro Firefox extension.

## Features
- ✅ Native Messaging bridge for Firefox
- ✅ Connects to local Ollama installation
- ✅ Cross-platform support (macOS, Windows, Linux)
- ✅ Privacy-first: All AI processing local

## Installation

See [README.md](https://github.com/yourusername/q-bookmark-ai-bridge#readme) for installation instructions.

## Requirements
- Q Book Marker Pro Firefox extension
- Ollama installed locally
- Python 3.7+

## What's Included
- `bridge.py` - Main bridge script
- `install.sh` - macOS/Linux installer
- `install.bat` - Windows installer
- `README.md` - Complete documentation
```

6. Click "Publish release"

### 4. Update Extension with Real GitHub URL

After creating the repository, update these files:

**In `/Users/johshaji/q-bookmark-manager/manager.html`:**
```html
<li>Download AI Bridge from <a href="https://github.com/YOURUSERNAME/q-bookmark-ai-bridge" target="_blank">GitHub</a></li>
```

**In `/Users/johshaji/q-bookmark-manager/manifest.json`:**
```json
"homepage_url": "https://github.com/YOURUSERNAME/q-bookmark-ai-bridge",
```

**In `/Users/johshaji/q-bookmark-ai-bridge/README.md`:**
```markdown
git clone https://github.com/YOURUSERNAME/q-bookmark-ai-bridge.git
```

Replace `YOURUSERNAME` with your actual GitHub username.

### 5. Rebuild Submission Package

```bash
cd /Users/johshaji/q-bookmark-manager
cp manifest.json manager.html mozilla-submission/
cd mozilla-submission
zip -r ../q-bookmark-pro-v1.2.0.zip *
```

### 6. Update Submission Guide

Update `FIREFOX_SUBMISSION_GUIDE.md` with the real GitHub URL in the description.

## Repository Settings (Optional but Recommended)

### Add Topics
Go to repository → About → Settings (gear icon) → Add topics:
- `firefox-extension`
- `ollama`
- `ai`
- `native-messaging`
- `bookmark-manager`
- `privacy`
- `local-ai`

### Add Description
```
AI Bridge for Q Book Marker Pro Firefox extension - enables local AI features via Ollama
```

### Add Website
```
https://addons.mozilla.org/firefox/addon/q-bookmark-pro/
```
(Update with actual Firefox Add-ons URL after approval)

## After GitHub Setup

1. ✅ Repository is public and accessible
2. ✅ Users can clone and install directly
3. ✅ Issues can be tracked on GitHub
4. ✅ Community can contribute
5. ✅ No email distribution needed

## Testing the Setup

1. Clone your repository in a different location
2. Run the installer
3. Verify it works with the extension
4. Check all links in README work

---

**Your GitHub Username:** _______________ (fill in)

**Repository URL:** https://github.com/_______________/q-bookmark-ai-bridge

**Ready to create the repository!**
