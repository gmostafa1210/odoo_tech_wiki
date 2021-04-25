from odoo import models, fields, api

class OwnerWiki(models.Model):
    _name = 'owner.wiki'
    _description = 'Owner Info'

    fname = fields.Char(string='First Name')
    lname = fields.Char(string='Last Name')
    name = fields.Char(string="Owner's Full Name", invisible='True', compute="_get_full_name")
    age = fields.Integer(string="Age", required='True', default='18')
    teenage = fields.Char(string="Teenage or Adult")
    infosaved = fields.Text(string="Other Information")
    img = fields.Binary(string="Photo", attachment=True)
    test = fields.Boolean('Test')

    company_id = fields.One2many('tech.wiki', 'owner_id', string="CEO of")

    food_id = fields.Many2many('food.wiki', string='Favourite Foods')

    def full_name(self):
        fname = ""
        lname = ""
        if self.fname:
            fname = self.fname
        if self.lname:
            lname = self.lname
        return fname + " " + lname

    def _get_full_name(self):
        for item in self:
            item.name = item.full_name()

    @api.onchange('fname','lname')
    def onchange_name(self):
        self.name = self.full_name()

    @api.onchange('age')
    def onchange_age(self):
        if self.age >= 13 and self.age <= 19:
            self.teenage = 'Teenager'
        elif self.age < 13:
            self.teenage = 'Under Age'
        else:
            self.teenage = 'Adult'

    @api.model
    def create(self, values):
        if not values['infosaved']:
            values['infosaved'] = 'Not Given'

        return super(OwnerWiki, self).create(values)

    def write(self, values):
        if 'infosaved' in values.keys() and not values['infosaved']:
            values['infosaved'] = 'Not Given'

        return super(OwnerWiki, self).write(values)
