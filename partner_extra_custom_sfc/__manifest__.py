{
    'name': 'partner_extra_custom_sfc',
    'author': 'SFC C.A',
    'version': '0.1',
    'category': 'Custom',
    'summary': 'Adds extra fields to the partner form.',
    'description': """
        <h2>Partner Extra Custom SFC</h2>
        <p>Este módulo añade campos adicionales para teléfono y correo electrónico en el formulario de contactos en Odoo, mejorando la gestión de la información.</p>
        <p><strong>Características:</strong></p>
        <ul>
            <li>Añade un campo de teléfono adicional.</li>
            <li>Añade un campo de correo electrónico adicional.</li>
            <li>Se integra con el módulo de contactos existente.</li>
        </ul>
        <p><strong>Instalación:</strong></p>
        <ol>
            <li>Clona el repositorio en tu sistema local.</li>
            <li>Copia la carpeta del módulo en el directorio de addons de Odoo.</li>
            <li>Reinicia el servidor de Odoo.</li>
            <li>Ve a la interfaz de Odoo y actualiza la lista de módulos.</li>
            <li>Busca "Partner Extra Custom SFC" y haz clic en Instalar.</li>
        </ol>
        <p><strong>Autor:</strong> SFC C.A - <a href="mailto:abcy775@gmail.com">abcy775@gmail.com</a></p>
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
