from odoo import models, fields


class TransitDriver(models.Model):
    _name = 'transit.driver'
    _description = 'Transit Driver'

    name = fields.Char(
        string='Driver Name',
        required=True
    )

    license_no = fields.Char(
        string='License Number',
        required=True
    )

    phone = fields.Char(
        string='Phone Number'
    )

    license_expiry = fields.Date(
        string='License Expiry'
    )

    status = fields.Selection([
        ('available', 'Available'),
        ('on_trip', 'On Trip'),
        ('inactive', 'Inactive')
    ], default='available')