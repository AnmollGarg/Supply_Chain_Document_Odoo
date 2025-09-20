from odoo import models, fields

class SupplyChainDocument(models.Model):
    _name = 'supply.chain.document'
    _description = 'Supply Chain Document'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    name = fields.Selection([
        ('certificate_of_origin', 'Certificate of Origin'),
        ('customs_document', 'Customs Document'),
        ('proof_of_delivery', 'Proof of Delivery'),
        ('proof_of_payment', 'Proof of Payment'),
        ('order_confirmation', 'Order Confirmation'),
        ('quotation', 'Quotation'),
        ('invoice', 'Invoice'),
        ('packing_slip', 'Packing Slip'),
        ('phytosanitary_certificate', 'Phytosanitary Certificate')
    ], string='Document Name', required=True)
    attachment_count = fields.Integer(string='Attachments', compute='_compute_attachment_count')
    status = fields.Selection([
        ('submitted', 'Submitted'),
        ('review', 'Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Document Status', default='submitted')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'supply_chain_document_attachment_rel',
        'document_id',
        'attachment_id',
        string='Attachments'
    )

    def _compute_attachment_count(self):
        for record in self:
            record.attachment_count = len(record.attachment_ids)

class SalesOrder(models.Model):
    _inherit = 'sale.order'
    scm_document_ids = fields.One2many('supply.chain.document', 'sale_order_id', string='Supply Chain Documents')
    scm_document_count = fields.Integer(string='SCM Docs Count', compute='_compute_scm_document_count')
    is_sales_person = fields.Boolean(
        string='Is Sales Person',
        compute='_compute_is_sales_person',
    )

    def _compute_scm_document_count(self):
        for order in self:
            order.scm_document_count = len(order.scm_document_ids)

    def _compute_is_sales_person(self):
        for record in self:
            record.is_sales_person = self.env.user.sales_person


