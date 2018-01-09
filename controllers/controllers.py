# -*- coding: utf-8 -*-
from odoo import http

# class Asignacion(http.Controller):
#     @http.route('/asignacion/asignacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asignacion/asignacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asignacion.listing', {
#             'root': '/asignacion/asignacion',
#             'objects': http.request.env['asignacion.asignacion'].search([]),
#         })

#     @http.route('/asignacion/asignacion/objects/<model("asignacion.asignacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asignacion.object', {
#             'object': obj
#         })