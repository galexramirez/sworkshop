# -*- coding: utf-8 -*-
# from odoo import http


# class Sworkshop(http.Controller):
#     @http.route('/sworkshop/sworkshop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sworkshop/sworkshop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sworkshop.listing', {
#             'root': '/sworkshop/sworkshop',
#             'objects': http.request.env['sworkshop.sworkshop'].search([]),
#         })

#     @http.route('/sworkshop/sworkshop/objects/<model("sworkshop.sworkshop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sworkshop.object', {
#             'object': obj
#         })

