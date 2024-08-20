# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class order(models.Model):
    _name = 'sworkshop.order'
    _description = 'Service Workshop Order'
    _order = 'id desc'

    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    owner_id = fields.Many2one("res.partner", string="Owner", required=True, related="customer_id", readonly=False)
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle", required=True)
    opening_date = fields.Datetime(string="Opening Date", required=True, copy=False, default=fields.Date.today)
    mobile = fields.Char(string="Mobile", related="customer_id.mobile", readonly=False)
    driver = fields.Many2one("res.partner", string="Driver")
    manager_id = fields.Many2one("res.users", string="Manager", index=True, tracking=True, default=lambda self: self.env.user)
    repairman_id = fields.Many2one("res.users", string="Repairman", required=True)
    helper_id = fields.Many2one("res.users", string="Helper")
    failures = fields.Text(string="Failures")
    duration = fields.Datetime(string="Duration", related="opening_date", required=True, readonly=False)
    deadline = fields.Datetime(string="Deadline")
    maintenance_types_id = fields.Many2one("sworkshop.maintenance.types", string="Maintenance Types")
    driving_test = fields.Boolean(string="Driving Test")
    status = fields.Selection(string="Status", selection=[('check_in','Check In'), ('check_out','Check Out'), ('in_quotation', 'In Quotation'), ('closed', 'Closed'), ('canceled','Canceled')], default="check_in", copy=False, readonly=True)
    lines_ids = fields.One2many("sworkshop.order.lines", "order_id", string="Order Lines")
    to_repair = fields.Text(string="To Repair")
    model_id = fields.Many2one("fleet.vehicle.model", string="Vehicle Model", related="vehicle_id.model_id")
    summary = fields.Text(string="Summary")
    
    @api.ondelete(at_uninstall=False)
    def _unlink_if_status_in_quotation_canceled(self):
        if any(record.status in ('check_out','in_quotation', 'closed') for record in self):
            raise UserError("Only check in o canceled orders can be deleted.")

    """ def action_set_status(self):
        if any(record.status == 'canceled' for record in self):
            raise UserError('Canceled order cannot be quoted.')
        self.update({'status': ''})
        return True """
    
    def action_set_cancel(self):
        if any(record.status == 'in-quotation' for record in self):
            raise UserError('Quoted order cannot be canceled.')
        self.update({'status': 'canceled'})
        return True
