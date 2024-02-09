# -*- coding: utf-8 -*-
{
    'name': "Febri Academy",

    'summary': "Module course technical odoo",

    'description': """
Module course technical odoo community 17 
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/teacher_level.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/data_course.xml',
         'reports/session.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

