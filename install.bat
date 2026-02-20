@echo off
REM Q Bookmark AI Bridge Installer for Windows

echo Q Bookmark AI Bridge Installer
echo ==================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python 3 is required but not installed.
    echo Please install Python 3 from python.org and try again.
    pause
    exit /b 1
)

echo Python found
python --version

REM Get script directory
set SCRIPT_DIR=%~dp0
set BRIDGE_SCRIPT=%SCRIPT_DIR%bridge.py

REM Manifest directory
set MANIFEST_DIR=%APPDATA%\Mozilla\NativeMessagingHosts
if not exist "%MANIFEST_DIR%" mkdir "%MANIFEST_DIR%"

REM Get extension ID
echo.
echo Enter your Q Bookmark extension ID:
echo (Find it in Firefox: about:debugging -^> This Firefox -^> Q Book Marker)
set /p EXTENSION_ID="Extension ID: "

if "%EXTENSION_ID%"=="" (
    echo ERROR: Extension ID is required
    pause
    exit /b 1
)

REM Create manifest (escape backslashes for JSON)
set BRIDGE_SCRIPT_JSON=%BRIDGE_SCRIPT:\=\\%
set MANIFEST_FILE=%MANIFEST_DIR%\com.qbookmark.aibridge.json

(
echo {
echo   "name": "com.qbookmark.aibridge",
echo   "description": "Q Bookmark AI Bridge",
echo   "path": "%BRIDGE_SCRIPT_JSON%",
echo   "type": "stdio",
echo   "allowed_extensions": ["%EXTENSION_ID%"]
echo }
) > "%MANIFEST_FILE%"

echo.
echo Bridge installed successfully!
echo.
echo Manifest location: %MANIFEST_FILE%
echo Bridge script: %BRIDGE_SCRIPT%
echo.
echo Next steps:
echo 1. Make sure Ollama is running
echo 2. Restart Firefox
echo 3. Open Q Bookmark Manager -^> Settings
echo 4. Enable AI features
echo.
echo Done!
pause
