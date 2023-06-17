# -*- coding: utf-8 -*-
# from odoo import http


# class MultiInvoiceApprovals(http.Controller):
#     @http.route('/multi_invoice_approvals/multi_invoice_approvals/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multi_invoice_approvals/multi_invoice_approvals/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('multi_invoice_approvals.listing', {
#             'root': '/multi_invoice_approvals/multi_invoice_approvals',
#             'objects': http.request.env['multi_invoice_approvals.multi_invoice_approvals'].search([]),
#         })

#     @http.route('/multi_invoice_approvals/multi_invoice_approvals/objects/<model("multi_invoice_approvals.multi_invoice_approvals"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multi_invoice_approvals.object', {
#             'object': obj
#         })
