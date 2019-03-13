# -*- coding: utf-8 -*-
from odoo import http

# class LunchObytes(http.Controller):
#     @http.route('/lunch__obytes/lunch__obytes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lunch__obytes/lunch__obytes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lunch__obytes.listing', {
#             'root': '/lunch__obytes/lunch__obytes',
#             'objects': http.request.env['lunch__obytes.lunch__obytes'].search([]),
#         })

#     @http.route('/lunch__obytes/lunch__obytes/objects/<model("lunch__obytes.lunch__obytes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lunch__obytes.object', {
#             'object': obj
#         })