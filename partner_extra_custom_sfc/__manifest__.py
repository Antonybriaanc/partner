{
    'name': 'partner_extra_custom_sfc',
    'author': 'SFC C.A',
    'version': '0.1',
    'category': 'Custom',
    'summary': 'Adds extra fields to the partner form.',
    'description': """
        <h2>Partner Extra Fields</h2>
        <p>El módulo <strong>Partner Extra Fields</strong> añade campos adicionales para teléfono y correo electrónico en el formulario de contacto de Odoo. Esta extensión es útil para mantener información adicional sobre los socios en un solo lugar.</p>
        <h3>Características:</h3>
        <ul>
            <li>Añade un campo de teléfono adicional.</li>
            <li>Añade un campo de correo electrónico adicional.</li>
            <li>Se integra con el módulo de contactos existente.</li>
        </ul>
        <h3>Instalación:</h3>
        <ol>
            <li>Clona el repositorio en tu sistema local.</li>
            <li>Copia la carpeta del módulo en el directorio de addons de Odoo.</li>
            <li>Reinicia el servidor de Odoo.</li>
            <li>Ve a la interfaz de Odoo y actualiza la lista de módulos.</li>
            <li>Busca <strong>Partner Extra Fields</strong> y haz clic en Instalar.</li>
        </ol>
        <h3>Uso:</h3>
        <p>Después de la instalación, los nuevos campos aparecerán en el formulario de contacto. Puedes completar los campos adicionales según sea necesario.</p>
        <h3>Contribuciones:</h3>
        <p>Las contribuciones son bienvenidas. Si deseas colaborar en este proyecto, sigue estos pasos:</p>
        <ol>
            <li>Haz un fork del repositorio.</li>
            <li>Crea una nueva rama (<code>git checkout -b feature/nueva-funcionalidad</code>).</li>
            <li>Realiza tus cambios y confirma los cambios (<code>git commit -m 'Añadida nueva funcionalidad'</code>).</li>
            <li>Sube tus cambios (<code>git push origin feature/nueva-funcionalidad</code>).</li>
            <li>Abre una pull request.</li>
        </ol>
        <h3>Licencia:</h3>
        <p>Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.</p>
        <h3>Autor:</h3>
        <p>SFC C.A - <a href="mailto:abcy775@gmail.com">abcy775@gmail.com</a></p>
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
