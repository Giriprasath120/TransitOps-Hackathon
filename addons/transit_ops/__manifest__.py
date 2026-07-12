{
    'name': 'Transit Operations',
    'version': '1.0',
    'category': 'Operations',
    'summary': 'Smart Transport Operations Management',
    'description': 'Fleet, Driver, Trip, Maintenance and Fuel Management',
    'author': 'Team TransitOps',

    'depends': ['base'],

    'data': [
    'security/ir.model.access.csv',

    'views/menu.xml',

    'views/vehicle_views.xml',
    'views/driver_views.xml',
    'views/trip_views.xml',
    'views/maintenance_views.xml',
    'views/fuel_log_views.xml',
],

    'installable': True,
    'application': True,
}