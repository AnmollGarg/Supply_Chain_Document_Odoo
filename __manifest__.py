{
    'name': 'Supply Chain Document Management',
    'version': '1.0',
    'summary': 'Manage and track supply chain documents efficiently',
    'description': """
        This module provides functionalities to manage and track supply chain documents such as invoices, delivery notes,
        and purchase orders. It integrates with existing Odoo modules to enhance document handling in the supply chain process.
    """,
    'category': 'Operations/Supply Chain',
    'depends': ['base', 'stock', 'purchase', 'account'],
    'data': [
        'views/supply_chain_document_views.xml',
        # 'views/supply_chain_document_user.xml',
        'security/ir.model.access.csv',
    ],
}