from odoo import models, fields
import calendar

class TechWiki(models.Model):
    _name = 'tech.wiki'
    _description = 'Technology'

    name = fields.Char(string='Company Name')
    foundation = fields.Date(string='Date of Foundation')
    country = fields.Selection([('american', 'American'), 
                                ('not_american', 'Not American')], 
                                default='american')
    address = fields.Text(string='Address')
    have_address = fields.Boolean(string='Have Address')
    logo = fields.Binary(string="Company Logo", attachment=True)

    owner_id = fields.Many2one('owner.wiki', string='Owner Name', domain=[('test','=',True)])

