
{
    'name': 'UnitSoft NavBar Branding Logo',
    'summary': 'Odoo Community NavBar Branding Logo',
    'version': '16.0.0.1',
    'category': 'Themes/Backend',
    'license': 'LGPL-3',
    'author': 'UnitSoft',
    'website': 'https://www.unitsoft.io',
    'description': """
        Odoo Community NavBar Branding Logo.
    """,
    'contributors': [
        'Suport <support@unitsoft.io>',
        ],
    'data': [
        ],
    'depends': [
        ],
    'assets': {
        'web.assets_backend': [
            'us_navbar_branding_logo/static/src/webclient/navbar/navbar.xml',
        ],
    },
    'images': ['static/description/banner.png'],

    'installable': True,
    'application': False,
    'auto_install': False,
}
