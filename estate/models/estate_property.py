from odoo import fields, models, api
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
    garden_area = fields.Integer('Garden Area')
    total_area = fields.Integer('Total Area', compute='_compute_total_area', store=True)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
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
    property_type_id = fields.Many2one('estate.property.type', 'Property Type')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', 'Offers')
    best_price = fields.Float(string="Best Offer", compute="_compute_best_price", store=True)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         'The name of the property should not be the description'),
        ('price_check',
         'CHECK(expected_price >= selling_price)',
         'The expected price must be greater than the selling price'),
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for property in self:
            property.best_price = property.offer_ids and max(property.offer_ids.mapped('price'), default=0)