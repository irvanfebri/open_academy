# -*- coding: utf-8 -*-
{
    'name': "perpustakaan",

    'summary': "Module Perpus Techinical Odoo",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','sale','website_payment','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/book.xml',
        'views/transaction.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/sale.xml',
        'views/generate_book.xml',
        'views/picking.xml',
        'data/sequence.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

