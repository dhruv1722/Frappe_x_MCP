"""Compatibility import for the Sales MCP tool registry.

New module-scoped entrypoints register through :mod:`mcp_erpnext.modules`.
"""

from __future__ import annotations

from typing import Any

from ..modules.sales import register_sales_tools


def register_tools(mcp: Any) -> None:
	"""Register the legacy catalog, now explicitly owned by Sales."""
	register_sales_tools(mcp)
