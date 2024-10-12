from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    aka_name = fields.Char(string='Extra Name', tracking=True)
    extra_phone_ids = fields.One2many('res.partner.phones','partner_id', string="Extra Phones")
    extra_email_ids = fields.One2many('res.partner.emails','partner_id', string="Extra Emails")
