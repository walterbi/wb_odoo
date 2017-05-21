# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ViewDesign(models.Model):
    _name = "library.book"

    name = fields.Char("Book name")
    qty = fields.Integer("Book quantity")
