# -*- coding: utf-8 -*-
# from odoo import http


# class Febriacademy(http.Controller):
#     @http.route('/febriacademy/febriacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/febriacademy/febriacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('febriacademy.listing', {
#             'root': '/febriacademy/febriacademy',
#             'objects': http.request.env['febriacademy.febriacademy'].search([]),
#         })

#     @http.route('/febriacademy/febriacademy/objects/<model("febriacademy.febriacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('febriacademy.object', {
#             'object': obj
#         })

