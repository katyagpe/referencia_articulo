# -*- coding: utf-8 -*-
{
    'name': "Hydro_asignacion",

    'summary': """ """,

    'description': """
        
    """,

    'author': "Katya Guadalupe Salas Rodríguez",
    'website': "http://www.cuartoangulo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}