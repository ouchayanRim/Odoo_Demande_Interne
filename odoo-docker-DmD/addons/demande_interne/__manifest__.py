{
    'name': 'Demandes Internes DmD',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Module de gestion des demandes internes pour le TP',
    'author': 'Votre Nom',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv', # Indispensable pour voir le bouton "Nouveau"
        'views/demande_views.xml',     # Indispensable pour voir les menus et le formulaire
    ],
    'assets': {
        'web.assets_backend': [
            'demande_interne/static/src/scss/style.scss',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}