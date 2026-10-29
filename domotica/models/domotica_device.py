# -*- coding: utf-8 -*-
# Copyright (c) 2026 Callista <https://www.callista.be>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models

class DomoticaDevice(models.Model):
    _name = "domotica.device"
    _description = "Domotica Device"
    _inherit = [
        'mail.thread',
    ]

    name = fields.Char(default="New", required=True)
    kind_of_domotica = fields.Many2one("domotica.kind", required=True)
    ip_address = fields.Char(required=True, tracking=True)
    is_online = fields.Boolean(default=True)

    def action_check_connectivity(self):
        self.is_online = not self.is_online

