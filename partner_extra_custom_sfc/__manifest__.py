{
    'name': 'partner_extra_custom_sfc',
    'author': 'SFC C.A',
    'version': '0.1',
    'category': 'Custom',
    'summary': 'Adds extra fields to the partner form.',
    'installable': True,
    'application': False,
    'depends': [
        'base',
        'mail',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'static/description/icon.png',
        'static/description/screenshot1.png',
        'static/description/screenshot2.png',
    ],
    'price': 19.99,
    'currency': 'USD',
    'license': 'LGPL-3',
}
