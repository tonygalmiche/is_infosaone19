# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 19 pour infosaone.com',
    'version'  : '19.0.0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 19 pour infosaone.com
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'website',
        'website_blog',
    ],
    'data' : [
        'views/ir_ui_view_views.xml',
        'views/website_footer.xml',
        'views/website_header.xml',
        'views/website_contact.xml',
        'views/website_branding.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
