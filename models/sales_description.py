from odoo import models, fields, api
import calendar

class SalesDescription(models.Model):
    _inherit = 'sale.order'

    sales_description = fields.Text(string='Note on Customer')

    @api.model
    def create(self, values):
        if not values['sales_description']:
            values['sales_description'] = 'Not Given'

        return super(SalesDescription, self).create(values)

    def write(self, values):
        if 'sales_description' in values.keys() and not values['sales_description']:
            values['sales_description'] = 'Not Given'

        return super(SalesDescription, self).write(values)

