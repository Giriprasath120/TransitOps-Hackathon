from odoo import models, fields


class TransitFuelLog(models.Model):
    _name = 'transit.fuel.log'
    _description = 'Fuel Log'

    vehicle_id = fields.Many2one(
        'transit.vehicle',
        string='Vehicle',
        required=True
    )

    fuel_date = fields.Date(
        string='Fuel Date'
    )

    liters = fields.Float(
        string='Fuel (Liters)'
    )

    amount = fields.Float(
        string='Amount'
    )

    odometer = fields.Float(
        string='Odometer Reading'
    )