# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, timedelta
from odoo import Command

SWORKSHOP_ORDER_STATE = [
    ("new", "Check In"),
    ("check_out", "Check Out"), 
    ("quote", "Quote"),
    ("work_order", "Work Order"), 
    ("close", "Closed"), 
    ("cancel", "Cancelled")
]

SWORKSHOP_ORDER_TYPE = [
    ("car", "Car"),
    ("motor", "Motor")
]

class Order(models.Model):
    _name = 'sworkshop.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Service Workshop Order'
    _check_company_auto = True

    name = fields.Char(
        string="Order Reference",
        required=True, copy=False, readonly=True,
        default='New')
    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True, index=True,
        default=lambda self: self.env.company)
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    owner_id = fields.Many2one("res.partner", string="Owner", required=True, related="customer_id", readonly=False)
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    opening_date = fields.Datetime(string="Opening Date", required=True, copy=False, default=fields.Date.today)
    mobile = fields.Char(string="Mobile", related="customer_id.mobile", readonly=False)
    driver_id = fields.Many2one("res.partner", string="Driver")
    manager_id = fields.Many2one("res.users", string="Manager", index=True, tracking=True, default=lambda self: self.env.user)
    master_chief_id = fields.Many2one("res.users", string="Master Chief")
    technician_id = fields.Many2one("res.users", string="Technician")
    failures = fields.Text(string="Failures")
    duration = fields.Datetime(string="Duration", related="opening_date", required=True, readonly=False)
    deadline = fields.Datetime(string="Deadline")
    maintenance_types_id = fields.Many2one("sworkshop.maintenance.types", string="Maintenance Types")
    driving_test = fields.Boolean(string="Driving Test")
    state = fields.Selection(string="Status", selection=SWORKSHOP_ORDER_STATE, default="new", copy=False, readonly=True, group_expand='_expand_states', index=True)
    lines_ids = fields.One2many("sworkshop.order.line", "order_id", string="Order Lines")
    to_repair = fields.Text(string="To Repair")
    model_id = fields.Many2one("fleet.vehicle.model", string="Vehicle Model", related="vehicle_id.model_id")
    summary = fields.Text(string="Summary")
    note = fields.Html(string="Note")
    image_vehicle = fields.Binary(string="Image")
    order_type = fields.Selection(string="Order Type", selection=SWORKSHOP_ORDER_TYPE, default="car", required=True, copy=False)
    reference_document = fields.Char(String="Reference Document")
    
    @api.ondelete(at_uninstall=False)
    def _unlink_if_status_in_quotation_canceled(self):
        if any(record.state in ('check_out','quote', 'work_order', 'close') for record in self):
            raise UserError("Only check in o canceled orders can be deleted.")

    def action_set_cancel(self):
        if any(record.state in ('close','cancel') for record in self):
            raise UserError('WorkShop Order cannot be canceled.')
        self.update({'state': 'cancel'})
        return True

    def action_set_status(self):
        return True
    
    def set_line_number(self):
        sl_no = 0
        for line in self.lines_ids:
            sl_no += 1
            line.sl_no = sl_no
        return
        
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' in vals:
                self = self.with_company(vals['company_id'])
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'sworkshop.order') or 'New'
        result = super(Order, self).create(vals_list)
        result.set_line_number()
        return result
    
    def write(self, values):
        res = super(Order, self).write(values)
        self.set_line_number()
        return res
        
    @api.onchange("vehicle_id")
    def _onchange_vehicle_id(self):
        self.customer_id = self.vehicle_id.owner_id

    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]