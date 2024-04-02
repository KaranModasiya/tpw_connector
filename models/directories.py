from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError

class Directories(models.Model):
	_name = 'directories'
	_description = 'Directory path of ftp server'

	tpw_id = fields.Many2one('tpw', string='TPW')
	path = fields.Char(string='Path')
