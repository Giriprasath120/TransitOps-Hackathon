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
    ],

    'installable': True,
    'application': True,
}