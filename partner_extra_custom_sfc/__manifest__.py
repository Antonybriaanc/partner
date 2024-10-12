{
    'name': 'partner_extra_custom_sfc',
    'author': 'SFC C.A',
    'version': '0.1',
    'category': 'Custom',
    'summary': 'Adds extra fields to the partner form.',
    'description': """
        <h2>Partner Extra Custom SFC</h2>
        <p>Este módulo añade campos adicionales al formulario de contactos en Odoo, mejorando la gestión de la información.</p>
        <h3>Características:</h3>
        <ul>
            <li>Campo extra 1: Detalles específicos</li>
            <li>Campo extra 2: Información adicional</li>
            <li>Integración con el módulo de contactos</li>
            <li>Mejora de la comunicación a través del módulo de correo</li>
        </ul>
        <p>Con este módulo, podrás gestionar mejor la información de tus clientes y contactos, agregando los campos que necesitas para personalizar tu sistema Odoo.</p>
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
    'images': ['static/description/cover_image.png'],
    'price': 19.99,
    'currency': 'USD',
    'license': 'LGPL-3',
}
