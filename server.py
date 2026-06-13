# server.py
from fastmcp import FastMCP

from tools.text_tools import (
    word_count,
    reverse_text,
    text_to_uppercase,
    text_to_lowercase,
    count_vowels,
    count_character,
    character_frequency,
    extract_emails,
    generate_password,
)
from tools.math_tools import (
    basic_calculator,
    unit_converter,
    prime_check,
)
from tools.todo_tools import (
    add_todo,
    list_todos,
    complete_todo,
    delete_todo,
    clear_completed,
)

# ── Create the MCP server ────────────────────────────────────────────────────
mcp = FastMCP(
    name="Personal Utility Toolkit",
    instructions="""
    A handy personal utility server with three categories of tools:

    📝 TEXT TOOLS  — analyze, transform, and extract from text
    🔢 MATH TOOLS  — calculator, unit conversion, prime factorization
    ✅ TODO TOOLS  — manage a persistent local todo list
    """,
)

# ── Register TEXT tools ──────────────────────────────────────────────────────
mcp.tool()(word_count)
mcp.tool()(reverse_text)
mcp.tool()(text_to_uppercase)
mcp.tool()(text_to_lowercase)
mcp.tool()(count_vowels)
mcp.tool()(count_character)
mcp.tool()(character_frequency)
mcp.tool()(extract_emails)
mcp.tool()(generate_password)

# ── Register MATH tools ──────────────────────────────────────────────────────
mcp.tool()(basic_calculator)
mcp.tool()(unit_converter)
mcp.tool()(prime_check)

# ── Register TODO tools ──────────────────────────────────────────────────────
mcp.tool()(add_todo)
mcp.tool()(list_todos)
mcp.tool()(complete_todo)
mcp.tool()(delete_todo)
mcp.tool()(clear_completed)


# ── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import os
    if os.environ.get("RAILWAY_ENVIRONMENT"):
        # Running on Railway → use HTTP transport
        port = int(os.environ.get("PORT", 8000))
        mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
    else:
        # Running locally → use stdio transport (Claude Desktop)
        mcp.run()
