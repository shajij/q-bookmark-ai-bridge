#!/usr/bin/env python3
"""
Q Bookmark AI Bridge
Native messaging host for Firefox extension to communicate with Ollama
"""
import sys
import json
import struct
import requests
from typing import Dict, Any

OLLAMA_URL = "http://localhost:11434"

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
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

def call_ollama(action: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Call Ollama API"""
    try:
        if action == "ping":
            return {"success": True, "message": "Bridge is running"}
        
        elif action == "summarize":
            bookmark = data.get("bookmark", {})
            model = data.get("model", "llama2")
            
            prompt = f"Summarize this bookmark in 2-3 sentences:\nTitle: {bookmark.get('title', '')}\nURL: {bookmark.get('url', '')}"
            
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
            query = data.get("query", "")
            bookmarks = data.get("bookmarks", [])
            model = data.get("model", "llama2")
            
            prompt = f"Given this search query: '{query}'\nFind the most relevant bookmarks from this list and explain why:\n"
            for i, bm in enumerate(bookmarks[:10]):  # Limit to 10
                prompt += f"{i+1}. {bm.get('title', '')} - {bm.get('url', '')}\n"
            
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
