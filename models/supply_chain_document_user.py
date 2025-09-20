from odoo import models, fields

class SupplyChainDDocumentUser(models.Model):
    _inherit = 'res.users'

    sales_person = fields.Boolean()