"""Explicit entrypoint for the Sales MCP server."""

from __future__ import annotations

from .mcp_server import create_mcp, main

__all__ = ("create_mcp", "main")


if __name__ == "__main__":
	main()
