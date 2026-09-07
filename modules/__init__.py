"""Controlled ERPNext MCP module registries."""

from __future__ import annotations

from typing import Any

SUPPORTED_MODULES = ("sales",)


def register_module_tools(module: str, mcp: Any) -> None:
	"""Register only the public tools belonging to one ERPNext module."""
	if module == "sales":
		from .sales import register_sales_tools

		register_sales_tools(mcp)
		return

	raise RuntimeError(f"MCP module '{module}' is not implemented.")
