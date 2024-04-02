
{
	'name': 'TPW Connector',
	'version': '1.0',
	'author': 'Karan Modasiya',
	'description': """
	This module is for Third Party Warehouse Management.
	""",
	'depends': ['sale_crm'],
	'data': [
		'security/ir.model.access.csv',

		'views/tpw_views.xml',
		# 'views/tpw_menus.xml',
		# 'wizard/views_validate_partial_stock_picking_wizard.xml',
		# 'wizard/record_cancellation_views.xml',
		# 'wizard/merge_sale_order_wizard_views.xml',
		]
}
