# -*- coding: utf-8 -*-
{
    'name': "Service Workshop",
    
    'summary': "Mechanical Workshop Management",

    'description': """
Administration and Management of services and resources for the care of a mechanical workshop
    """,

    'author': "Alexander Ramirez",
    'website': "https://www.conectiva.com.pe",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'fleet',
        'product',
        'mail',
        'stock'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        
        'data/ir_sequence_data.xml',
        
        'views/isw_mrp_bom_views.xml',
        'views/isw_res_users_views.xml',
        'views/sw_product_brand_views.xml',
        'views/sw_maintenance_types_views.xml',
        'views/isw_product_template_views.xml',
        'views/isw_fleet_vehicle_atypes_views.xml',
        'views/isw_fleet_vehicle_tags_views.xml',
        'views/sw_vehicle_state_views.xml',
        'views/isw_fleet_vehicle_stypes_views.xml',
        'views/isw_fleet_vehicle_categories_views.xml',
        'views/isw_fleet_vehicle_models_views.xml',
        'views/isw_fleet_vehicle_manufactures_views.xml',
        'views/isw_fleet_vehicle_views.xml',
        'views/sw_order_views.xml',
        'views/sw_menu_root.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False
}

