from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError

class TPW(models.Model):
	_name = 'tpw'
	_description = 'Third Party Warehouse Connector'

	partner_id = fields.Many2one('res.partner', string='TPW Partner', required=True)
	host = fields.Char(string="Host", help="Host name of the ftp server")
	port = fields.Integer(string="Port", help="Port of the ftp server")
	username = fields.Char(string="Username", help="Username of the ftp server")
	password = fields.Char(string="Password", help="Password of the ftp server")
	path_ids = fields.One2many('directories', inverse_name='tpw_id', string='Path', help="Path of the ftp server")
