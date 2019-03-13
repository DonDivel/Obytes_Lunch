# -*- coding: utf-8 -*-

from odoo import models, fields, api

 class option(models.Model):
     _name = 'lunch__obytes.option'
    _description = "Obaytes options"
    titre = fields.Text()
    type_ = fields.Text()
     value = fields.Text()

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100