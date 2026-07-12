from odoo import models, fields


class TransitMaintenance(models.Model):
    _name = 'transit.maintenance'
    _description = 'Vehicle Maintenance'

    vehicle_id = fields.Many2one(
        'transit.vehicle',
        string='Vehicle',
        required=True
    )

    service_date = fields.Date(
        string='Service Date'
    )

    description = fields.Text(
        string='Description'
    )

    cost = fields.Float(
        string='Cost'
    )

    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed')
    ], default='scheduled')