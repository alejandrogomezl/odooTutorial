from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _order = "name"

    name = fields.Char('Property Name', required=True)
    description = fields.Char('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From')
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], 'Garden Orientation')

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         'The name of the property should not be the description'),
        ('price_check',
         'CHECK(expected_price >= selling_price)',
         'The expected price must be greater than the selling price'),
    ]