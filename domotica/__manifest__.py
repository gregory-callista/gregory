# -*- coding: utf-8 -*-
# Copyright (c) 2026 Callista <https://www.callista.be>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Domotica",
    "version": "20.0.1.0.0",
    "summary": "Adds domotica management and control",
    "author": "Callista BV",
    "website": "https://www.callista.be",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "data/domotica_kind_data.xml",
        "security/ir.access.csv",
        "security/res_groups_data.xml",
        "views/domotica_device_views.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
