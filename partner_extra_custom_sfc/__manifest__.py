{
    'name': 'partner_extra_custom_sfc',
    'author': 'SFC C.A',
    'version': '0.1',
    'category': 'Custom',
    'summary': 'Adds extra fields to the partner form.',
    'description': """
        &lt;h2&gt;Partner Extra Custom SFC&lt;/h2&gt;
        &lt;p&gt;Este módulo añade campos adicionales al formulario de contactos en Odoo, mejorando la gestión de la información.&lt;/p&gt;
        &lt;h3&gt;Características:&lt;/h3&gt;
        &lt;ul&gt;
            &lt;li&gt;Campo extra 1: Detalles específicos&lt;/li&gt;
            &lt;li&gt;Campo extra 2: Información adicional&lt;/li&gt;
            &lt;li&gt;Integración con el módulo de contactos&lt;/li&gt;
            &lt;li&gt;Mejora de la comunicación a través del módulo de correo&lt;/li&gt;
        &lt;/ul&gt;
        &lt;p&gt;Con este módulo, podrás gestionar mejor la información de tus clientes y contactos, agregando los campos que necesitas para personalizar tu sistema Odoo.&lt;/p&gt;
    """,
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
    'images': ['static/description/screenshot1.png'],
    'price': 19.99,
    'currency': 'USD',
    'license': 'LGPL-3',
}
