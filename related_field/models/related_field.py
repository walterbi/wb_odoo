# -*- coding: utf-8 -*-

from odoo import fields, api, models


class RelatedField(models.Model):
    _inherit = "product.template"

    ascii_name = fields.Char(related="name")
