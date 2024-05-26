# -*- coding: utf-8 -*-
{
    'name': "Service Workshop",
    
    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Alexander Ramirez",
    'website': "https://www.conectiva.com.pe",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'fleet'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inherited_fleet_vehicle_views.xml',
        'views/sworkshop_order_views.xml',
        'views/sworkshop_menu_root.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'license': 'LGPL-3'
}

