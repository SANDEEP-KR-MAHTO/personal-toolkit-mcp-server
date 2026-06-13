# 🛠️ Personal Utility Toolkit — MCP Server

A local MCP server built with [FastMCP](https://github.com/jlowin/fastmcp)
that plugs directly into Claude Desktop.

## Tools

| Category | Tool | Description |
|----------|------|-------------|
| 📝 Text | `word_count` | Words, chars, sentences |
| 📝 Text | `reverse_text` | Reverse a string |
| 📝 Text | `text_to_uppercase` | Convert text to uppercase |
| 📝 Text | `text_to_lowercase` | Convert text to lowercase |
| 📝 Text | `count_vowels` | Count vowels and consonants |
| 📝 Text | `extract_emails` | Pull emails from text |
| 📝 Text | `generate_password` | Secure password generator |
| 🔢 Math | `basic_calculator` | Safe expression evaluator |
| 🔢 Math | `unit_converter` | Length / weight / temperature |
| 🔢 Math | `prime_check` | Primality + factorization |
| ✅ Todo | `add_todo` | Add a todo with priority |
| ✅ Todo | `list_todos` | Filter pending / done |
| ✅ Todo | `complete_todo` | Mark done by ID |
| ✅ Todo | `delete_todo` | Remove by ID |
| ✅ Todo | `clear_completed` | Wipe all completed todos |

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/local-mcp-server
cd local-mcp-server
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Connect to Claude Desktop

Add this block to your `claude_desktop_config.json`:

- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "personal-toolkit": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

> 💡 On Windows use `venv\\Scripts\\python.exe`

Restart Claude Desktop — you'll see the 🔨 tools icon appear!

## Try These Prompts

```
Count the words in: "The quick brown fox jumps over the lazy dog"
Calculate: sqrt(256) + 2 ** 8
Convert 100 miles to km
Add a high priority todo: "Learn MCP servers"
List all my pending todos
Is 97 a prime number?
Generate a 20-character password
Extract emails from: "contact john@example.com or jane@test.org"
```

## Project Structure

```
local-mcp-server/
├── server.py          # Main MCP server — tool registration & entry point
├── tools/
│   ├── __init__.py    # Makes tools/ a Python package
│   ├── text_tools.py  # Text utility functions
│   ├── math_tools.py  # Math / calculator functions
│   └── todo_tools.py  # Persistent todo list (todos.json)
├── requirements.txt
└── README.md
```
