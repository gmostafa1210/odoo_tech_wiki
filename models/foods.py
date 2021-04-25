from odoo import models, fields, api, _
from odoo.exceptions import UserError

class FoodWiki(models.Model):
    _name = 'food.wiki'
    _description = 'Food Info'
    _sql_constraints = [
        ('scode_uniq', 'unique (scode)', "Small Code Already exist.")
    ]

    name = fields.Char(string='Food Name')
    foodprice = fields.Float(string='Price')
    code = fields.Char(string='Code')
    scode = fields.Integer(string='Small Code')

    @api.model
    def create(self, values):
        if values['foodprice'] < 0:
            raise UserError ('Price can not be negative')
        else:
            return super(FoodWiki, self).create(values)

    def write(self, values):
        if values['foodprice'] and values['foodprice'] < 0:
            raise UserError ('Price can not be negative')
        else:
            return super(FoodWiki, self).write(values)

    def test_button_obj(self):
        #orm 
        all_data = self.env['tech.wiki'].search(['|',('owner_id', '=', self.id), ('country', '=', 'american')])
        for data in all_data:
            #print(data.name)
            if data.name == 'SpaceX':
                data.unlink()

        # obj = self.env['tech.wiki'].create({
        #     'name':'SpaceX',
        # })

        # obj.write({
        #     'name' : 'OpenAI',
        # })

        self.env.cr.execute("""select name from tech_wiki;""",)
        sql_data = self.env.cr.fetchall()
        
        raise UserError (_(sql_data))

    @api.onchange('code')
    def onchange_code(self):
        all_code = self.env['food.wiki'].search([])
        if self.code:
            for val in all_code:
                if self.code == val.code:
                    raise UserError(_("Code Already exist."))

    def write(self, values):
        all_codes = self.env ['food.wiki'].search([('code', '=', values['code'])])
        if all_codes:
            raise UserError(_("Code Already exist."))
        return super(FoodWiki, self).write(values)

    @api.model 
    def create(self, values):
        all_codes = self.env ['food.wiki'].search([('code', '=', values['code'])])
        if all_codes:
            raise UserError(_("Code Already exist."))
        return super(FoodWiki, self).create(values)
