# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################

{
    "name": "Docuware Connector",
    "version": "14.0.2.0.0",
    "category": "Documentation",
    "author": "PedroGuirao",
    "maintainer": "Serincloud",
    "website": "www.ingenieriacloud.com",
    "license": "AGPL-3",
    "depends": [
        'mail',
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/docuware_sync_cabinets.xml',
        'views/views_models.xml',
        'views/views_menu.xml',
        'views/res_company_views.xml',
    ],
    "installable": True,
}
