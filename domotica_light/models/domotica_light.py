# -*- coding: utf-8 -*-
# Copyright (c) 2026 Callista <https://www.callista.be>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models

class DomoticaLight(models.Model):
    _name = "domotica.light"
    _description = "Domotica Light"
    _inherit = "domotica.device"

    is_light = fields.Boolean(default=False)