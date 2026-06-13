# 🛠️ Personal Utility Toolkit — MCP Server

A **remote MCP server** built with [FastMCP](https://github.com/jlowin/fastmcp) and deployed on Railway.
Plug it into Claude Desktop and get 17 utility tools instantly — no setup, no local dependencies.

---

## ⚡ Quick Connect (Remote — No Installation Needed)

Add this to your `claude_desktop_config.json`:

**Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "personal-toolkit-remote": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://web-production-2f9c2.up.railway.app/mcp"]
    }
  }
}
```

> **Requires:** [Node.js](https://nodejs.org) installed on your machine.  
> Restart Claude Desktop after saving — that's it! 🎉

---

## 🧰 Available Tools

### 📝 Text Tools
| Tool | Description |
|------|-------------|
| `word_count` | Count words, characters, sentences, paragraphs |
| `reverse_text` | Reverse any string |
| `text_to_uppercase` | Convert text to UPPERCASE |
| `text_to_lowercase` | Convert text to lowercase |
| `count_vowels` | Count vowels and consonants |
| `count_character` | Count occurrences of a specific character |
| `character_frequency` | Frequency of every character ranked by count |
| `extract_emails` | Pull all email addresses from a block of text |
| `generate_password` | Generate a secure random password |

### 🔢 Math Tools
| Tool | Description |
|------|-------------|
| `basic_calculator` | Safely evaluate math expressions (`sqrt`, `log`, `sin`, etc.) |
| `unit_converter` | Convert length, weight, and temperature units |
| `prime_check` | Check if a number is prime + get its factors |

### ✅ Todo Tools
| Tool | Description |
|------|-------------|
| `add_todo` | Add a todo with priority (low / medium / high) |
| `list_todos` | List all, pending, or completed todos |
| `complete_todo` | Mark a todo as done by ID |
| `delete_todo` | Delete a todo by ID |
| `clear_completed` | Remove all completed todos |

---

## 💬 Example Prompts

```
Count the words in: "The quick brown fox jumps over the lazy dog"
Calculate: sqrt(256) + 2 ** 10
Convert 100 miles to km
Is 97 a prime number?
Generate a 20-character password with symbols
Extract emails from: "contact john@example.com or jane@test.org"
Add a high priority todo: "Learn MCP servers"
List all my pending todos
```

---

## 🏃 Run Locally

If you want to run your own instance:

```bash
git clone https://github.com/SANDEEP-KR-MAHTO/personal-toolkit-mcp-server.git
cd personal-toolkit-mcp-server
python -m venv venv
venv\Scripts\activate          # Windows (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

Add to `claude_desktop_config.json`:

**Windows:**
```json
{
  "mcpServers": {
    "personal-toolkit-local": {
      "command": "C:\\path\\to\\venv\\Scripts\\python.exe",
      "args": ["C:\\path\\to\\server.py"]
    }
  }
}
```

**Mac/Linux:**
```json
{
  "mcpServers": {
    "personal-toolkit-local": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

---

## 🚀 Deploy Your Own on Railway

1. Fork this repo
2. Go to [railway.app](https://railway.app) → **New Project** → **GitHub Repo**
3. Select your fork → **Deploy**
4. Go to **Settings → Networking → Generate Domain**
5. Update the URL in your `claude_desktop_config.json`

---

## 🗂️ Project Structure

```
├── server.py          # MCP server entry point
├── tools/
│   ├── text_tools.py  # Text utility functions
│   ├── math_tools.py  # Math functions
│   └── todo_tools.py  # Persistent todo list (todos.json)
├── Procfile           # Railway start command
└── requirements.txt
```

---

## 🛠️ Built With

- [FastMCP](https://github.com/jlowin/fastmcp) — MCP server framework
- [Railway](https://railway.app) — Deployment platform
- [mcp-remote](https://github.com/geelen/mcp-remote) — HTTP→stdio bridge for Claude Desktop
