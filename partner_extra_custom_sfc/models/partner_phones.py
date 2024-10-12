from odoo import api, models, fields

class PartnerPhones(models.Model):
    _name = 'res.partner.phones'
    _description = 'Extra Partner Phones'
    
    name = fields.Char(string='Phone', required=True)
    notes = fields.Char(string='Notes')
    partner_id = fields.Many2one('res.partner', string="Partner", readonly=True)