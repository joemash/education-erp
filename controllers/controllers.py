# -*- coding: utf-8 -*-
from odoo import http

# class WinguSchool(http.Controller):
#     @http.route('/wingu_school/wingu_school/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wingu_school/wingu_school/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wingu_school.listing', {
#             'root': '/wingu_school/wingu_school',
#             'objects': http.request.env['wingu_school.wingu_school'].search([]),
#         })

#     @http.route('/wingu_school/wingu_school/objects/<model("wingu_school.wingu_school"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wingu_school.object', {
#             'object': obj
#         })