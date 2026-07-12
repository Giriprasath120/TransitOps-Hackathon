from odoo import models, fields


class TransitVehicle(models.Model):
    _name = 'transit.vehicle'
    _description = 'Transit Vehicle'

    registration_no = fields.Char(
        string='Registration Number',
        required=True
    )

    vehicle_name = fields.Char(
        string='Vehicle Name',
        required=True
    )

    vehicle_type = fields.Selection([
        ('truck', 'Truck'),
        ('bus', 'Bus'),
        ('van', 'Van')
    ], string='Vehicle Type')

    capacity = fields.Float(
        string='Capacity'
    )

    status = fields.Selection([
        ('available', 'Available'),
        ('on_trip', 'On Trip'),
        ('maintenance', 'Maintenance')
    ], default='available')

    purchase_date = fields.Date(
        string='Purchase Date'
    )