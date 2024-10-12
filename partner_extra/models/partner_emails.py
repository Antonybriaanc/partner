from odoo import api, models, fields

class PartnerEmails(models.Model):
    _name = 'res.partner.emails'
    _description = 'Extra Partner Phones'
    
    name = fields.Char(string='Emails', required=True)
    notes = fields.Char(string='Notes')
    partner_id = fields.Many2one('res.partner', string="Partner", readonly=True)