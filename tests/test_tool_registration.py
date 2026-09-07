from __future__ import annotations

import unittest

from mcp_erpnext.modules import register_module_tools


class RecordingMCP:
	"""Minimal FastMCP-compatible recorder for static registration verification."""

	def __init__(self):
		self.tool_names: list[str] = []

	def tool(self):
		def decorator(function):
			self.tool_names.append(function.__name__)
			return function

		return decorator


class ToolRegistrationTests(unittest.TestCase):
	def test_sales_module_registers_only_the_controlled_sales_workflow_tools(self):
		mcp = RecordingMCP()
		register_module_tools("sales", mcp)

		self.assertEqual(
			mcp.tool_names,
			[
				"search_customers",
				"resolve_customer",
				"prepare_customer",
				"confirm_customer",
				"search_items",
				"resolve_item",
				"prepare_item",
				"confirm_item",
				"prepare_sales_order",
				"confirm_sales_order",
				"prepare_quotation",
				"confirm_quotation",
			],
		)
