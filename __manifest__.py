# -*- coding: utf-8 -*-
{
    'name': "lunch__obytes",

    'summary': """
        Lunch Modul by Obytes""",

    'description': """
        Custm Lunch Modul By Obytes
    """,

    'author': "Hdia Saad",
    'website': "http://www.Obytes.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/lunch__obytes.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}