from odoo import models, fields


class TransitTrip(models.Model):
    _name = 'transit.trip'
    _description = 'Transit Trip'

    trip_name = fields.Char(
        string='Trip Name',
        required=True
    )

    source = fields.Char(
        string='Source',
        required=True
    )

    destination = fields.Char(
        string='Destination',
        required=True
    )

    vehicle_id = fields.Many2one(
        'transit.vehicle',
        string='Vehicle'
    )

    driver_id = fields.Many2one(
        'transit.driver',
        string='Driver'
    )

    distance = fields.Float(
        string='Distance (KM)'
    )

    start_date = fields.Datetime(
        string='Start Time'
    )

    end_date = fields.Datetime(
        string='End Time'
    )

    status = fields.Selection([
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='planned')