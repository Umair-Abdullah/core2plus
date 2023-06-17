# -*- coding: utf-8 -*-
{
    'name': "Multi Invoice Approvals",

    'summary': """Thais App is used for 2 Level Invoice Approval""",

    'description': """
        Thais App is used for 2 Level Invoice Approval
    """,

    'author': "UTech",
    'website': "https://www.linkedin.com/in/umair-abdullah/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Accounting',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/email.xml',
        'security/security.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
