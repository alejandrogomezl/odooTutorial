from odoo import fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "name"

    name = fields.Char('Property Type', required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id', 'Properties')
    sequence = fields.Integer('Sequence', default=10)

    _sql_constraints = [
        ('unique_property_type_name', 'UNIQUE(name)', 'The property type name must be unique.'),
    ]