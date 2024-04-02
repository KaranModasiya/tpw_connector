from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError

class TransferData(models.TransientModel):
	_name = 'transfer.data.wizard'

	tpw_id = fields.Many2one('tpw', string='TPW Partner')
	operation_type = fields.Selection([
		('Import', 'Import'),
		('Export', 'Export')
	], string='Operation Type', help="The type of the Operation")
	operation = fields.Many2one('directories', string='Operation', help="The path for the operation")
	product_ids = fields.Many2many('product.template', string='Product')
	sale_picking_ids = fields.Many2many('stock.picking', string='Sale Order Pickings')
	purchase_picking_ids = fields.Many2many('stock.picking', string='Purchase Order Pickings')

	def action_execute(self):
		pass
