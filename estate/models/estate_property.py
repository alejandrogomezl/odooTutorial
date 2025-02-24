from odoo import fields, models
from datetime import date, timedelta

class Property(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _order = "name"

    name = fields.Char('Property Name', required=True, default='Unknown')
    description = fields.Char('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From', default=lambda self: date.today() + timedelta(days=90))
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms', default=2)
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    active = fields.Boolean('Active', default=True)
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], 'Garden Orientation')
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], 'Status', default='new')
    salesperson_id = fields.Many2one('res.users', 'Sales Person', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', 'Buyer')

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         'The name of the property should not be the description'),
        ('price_check',
         'CHECK(expected_price >= selling_price)',
         'The expected price must be greater than the selling price'),
    ]