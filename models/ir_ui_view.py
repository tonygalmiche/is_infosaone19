# -*- coding: utf-8 -*-

from odoo import models, fields


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    is_origine_view_id = fields.Integer(string="Origine View ID")
