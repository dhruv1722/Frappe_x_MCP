"""Sales MCP tool registry."""

from __future__ import annotations

from typing import Any


def register_sales_tools(mcp: Any) -> None:
	"""Register the Sales MCP's master and selling workflows."""
	from ..tools.masters.customer import register_customer_tools
	from ..tools.masters.item import register_item_tools
	from ..tools.selling.quotation import register_quotation_tools
	from ..tools.selling.sales_order import register_sales_order_tools

	register_customer_tools(mcp)
	register_item_tools(mcp)
	register_sales_order_tools(mcp)
	register_quotation_tools(mcp)
