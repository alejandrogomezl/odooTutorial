from odoo import fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "name"

    name = fields.Char('Property Type', required=True)
