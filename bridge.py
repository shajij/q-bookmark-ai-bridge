#!/usr/bin/env python3
"""
Q Bookmark AI Bridge v1.1.0
Native messaging host for Firefox extension to communicate with Ollama

Security improvements:
- Input sanitization to prevent prompt injection
- 1MB message size limit to prevent DoS
- Localhost-only Ollama connection
"""
import sys
import json
import struct

# Try to import requests, provide helpful error if missing
try:
    import requests
except ImportError:
    error_msg = {
        "success": False, 
        "error": "Python 'requests' module not installed. Run: pip3 install --break-system-packages requests"
    }
    encoded = json.dumps(error_msg).encode('utf-8')
    sys.stdout.buffer.write(struct.pack('I', len(encoded)))
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()
    sys.exit(1)

from typing import Dict, Any
import re

OLLAMA_URL = "http://localhost:11434"
MAX_INPUT_LENGTH = 10000  # Maximum characters for any input
MAX_BOOKMARKS = 50  # Maximum bookmarks to process
MAX_MESSAGE_SIZE = 1024 * 1024  # 1MB maximum message size

def sanitize_input(text: str, max_length: int = MAX_INPUT_LENGTH) -> str:
    """Sanitize user input to prevent prompt injection"""
    if not text:
        return ""
    # Limit length
    text = text[:max_length]
    # Remove control characters
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    # Escape potential prompt injection attempts
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text.strip()

def send_message(message: Dict[str, Any]):
    """Send message to Firefox extension"""
    encoded = json.dumps(message).encode('utf-8')
    sys.stdout.buffer.write(struct.pack('I', len(encoded)))
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()

def read_message() -> Dict[str, Any]:
    """Read message from Firefox extension"""
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        return None
    message_length = struct.unpack('I', raw_length)[0]
    
    # Reject messages larger than 1MB
    if message_length > MAX_MESSAGE_SIZE:
        send_message({"success": False, "error": "Message too large (max 1MB)"})
        return None
    
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

def call_ollama(action: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Call Ollama API"""
    try:
        if action == "ping":
            return {"success": True, "message": "Bridge is running"}
        
        elif action == "summarize":
            bookmark = data.get("bookmark", {})
            model = data.get("model", "llama3")
            
            # Sanitize inputs
            title = sanitize_input(bookmark.get('title', ''), 500)
            url = sanitize_input(bookmark.get('url', ''), 2000)
            
            prompt = f"Summarize this bookmark in 2-3 sentences:\nTitle: {title}\nURL: {url}"
            
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return {"success": True, "result": result.get("response", "")}
            else:
                return {"success": False, "error": f"Ollama error: {response.status_code}"}
        
        elif action == "search":
            query = sanitize_input(data.get("query", ""), 500)
            bookmarks = data.get("bookmarks", [])[:MAX_BOOKMARKS]  # Limit bookmarks
            model = data.get("model", "llama3")
            
            prompt = f"Given this search query: '{query}'\nFind the most relevant bookmarks from this list and explain why:\n"
            for i, bm in enumerate(bookmarks[:10]):  # Limit to 10 for display
                title = sanitize_input(bm.get('title', ''), 200)
                url = sanitize_input(bm.get('url', ''), 500)
                prompt += f"{i+1}. {title} - {url}\n"
            
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return {"success": True, "result": result.get("response", "")}
            else:
                return {"success": False, "error": f"Ollama error: {response.status_code}"}
        
        else:
            return {"success": False, "error": f"Unknown action: {action}"}
    
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "Cannot connect to Ollama. Is it running?"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    """Main loop"""
    while True:
        try:
            message = read_message()
            if message is None:
                break
            
            action = message.get("action", "")
            data = message.get("data", {})
            
            result = call_ollama(action, data)
            send_message(result)
        
        except Exception as e:
            send_message({"success": False, "error": str(e)})
            break

if __name__ == "__main__":
    main()
