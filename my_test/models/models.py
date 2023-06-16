# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MyViewTesting(models.Model):
    _name = 'my.view'

    name = fields.Char()
    all_sale_orders = fields.Many2many('sale.order')
    partner_id = fields.Many2one('res.partner')
    my_sales = fields.One2many('my.sales', 'my_view')

    def clear_list(self):
        self.my_sales.unlink()
        self.env['my.sales'].unlink()


    def get_records(self):
        # print('test')
        so = self.env['sale.order'].search([
            ('state', '=', ('draft','sale')),('partner_id', '=', self.partner_id.id),
        ])
        print(so)
        # self.env['my.sales'].create({
        #         'name': 6,
        #         'my_view': self.id
        #     })


        for rec in so:
            self.env['my.sales'].create({
                'name': rec.id,
                'my_view': self.id
            })



class MySaleOrderList(models.Model):
    _name = 'my.sales'
    #     _description = 'my_test.my_test'

    name = fields.Many2one('sale.order')
    partner_id = fields.Many2one(related='name.partner_id')
    sales_person = fields.Many2one(related='name.user_id')

    my_view = fields.Many2one('my.view')

