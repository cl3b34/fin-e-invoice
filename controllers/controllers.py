# -*- coding: utf-8 -*-
from odoo import http

# class Fin-e-invoice(http.Controller):
#     @http.route('/fin-e-invoice/fin-e-invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fin-e-invoice/fin-e-invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fin-e-invoice.listing', {
#             'root': '/fin-e-invoice/fin-e-invoice',
#             'objects': http.request.env['fin-e-invoice.fin-e-invoice'].search([]),
#         })

#     @http.route('/fin-e-invoice/fin-e-invoice/objects/<model("fin-e-invoice.fin-e-invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fin-e-invoice.object', {
#             'object': obj
#         })