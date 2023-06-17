# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class MultiInvoiceApprovals(models.Model):
    _inherit = 'account.move'
    #
    # no_of_consumers = fields.Integer(string='No Of Consumers')
    # recovered_account = fields.Integer(string='Recovered Amount')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('waiting_for_approval_1', 'Waiting For First Approval'),
        ('waiting_for_approval_2', 'Waiting For Second Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('posted', 'Approved'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')


    requested_by = fields.Many2one(
        comodel_name="res.users",
        string="Requested by",
        required=True,
        copy=False,
        track_visibility="onchange",
        default=lambda self: self.env.user

    )

    def submit_for_approval_1(self):
        for rec in self:
            rec.state = 'waiting_for_approval_1'

        # self.write({"state": "to_2_approve"})

        mail_server = self.env['ir.mail_server'].sudo().search([], limit=1)
        inv_manager = self.env.ref('multi_invoice_approvals.group_invoice_approval_1').users
        if inv_manager:
            ctx = {}
            if mail_server:
                ctx['email_from'] = mail_server.smtp_user
            else:
                pass
                ctx['email_from'] = self.requested_by.login
            email_list = [approver.login for approver in inv_manager]
            if email_list:
                ctx['notification_to_approvers'] = ','.join([email for email in email_list if email])
                ctx['approver_name'] = self.env.user.name
                template = self.env.ref('multi_invoice_approvals.first_approval_invoice_email_template')
                template.with_context(ctx).sudo().send_mail(self.id, force_send=True, raise_exception=False)

    def submit_for_approval_2(self):
        for rec in self:
            rec.state = 'waiting_for_approval_2'

        mail_server = self.env['ir.mail_server'].sudo().search([], limit=1)
        inv_manager = self.env.ref('multi_invoice_approvals.group_invoice_approval_2').users
        if inv_manager:
            ctx = {}
            if mail_server:
                ctx['email_from'] = mail_server.smtp_user
            else:
                pass
                ctx['email_from'] = self.requested_by.login
            email_list = [approver.login for approver in inv_manager]
            if email_list:
                ctx['notification_to_approvers'] = ','.join([email for email in email_list if email])
                ctx['approver_name'] = self.env.user.name
                template = self.env.ref('multi_invoice_approvals.second_approval_invoice_email_template')
                template.with_context(ctx).sudo().send_mail(self.id, force_send=True, raise_exception=False)


    def button_rejected(self):
        self.write({"state": "rejected"})

        mail_server = self.env['ir.mail_server'].sudo().search([], limit=1)
        ctx = {}
        if mail_server:
            ctx['email_from'] = mail_server.smtp_user
        else:
            ctx['email_from'] = self.requested_by.login
        email_list = [self.requested_by.login]
        if email_list:
            ctx['notification_to_initiator'] = ','.join([email for email in email_list if email])
            ctx['rejected_by'] = self.env.user.name
            template = self.env.ref('multi_invoice_approvals.invoice_approval_reject_email_template')
            template.with_context(ctx).sudo().send_mail(self.id, force_send=True, raise_exception=False)



    def action_post(self):
        # for rec in self:
        # rec.action_confirm()
        # rec.state = 'sale'
        res = super(MultiInvoiceApprovals, self).action_post()
        return res



