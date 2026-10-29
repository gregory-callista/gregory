# -*- coding: utf-8 -*-
# Copyright (c) 2026 Callista <https://www.callista.be>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models

class DomoticaKind(models.Model):
    _name = 'domotica.kind'
    _description = 'Domotica Kind'

    name = fields.Char(required=True)