# -*- coding: utf-8 -*-
# from odoo import http


# class TransitOps(http.Controller):
#     @http.route('/transit_ops/transit_ops', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transit_ops/transit_ops/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('transit_ops.listing', {
#             'root': '/transit_ops/transit_ops',
#             'objects': http.request.env['transit_ops.transit_ops'].search([]),
#         })

#     @http.route('/transit_ops/transit_ops/objects/<model("transit_ops.transit_ops"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transit_ops.object', {
#             'object': obj
#         })

