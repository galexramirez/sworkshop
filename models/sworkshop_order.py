# -*- coding: utf-8 -*-

from odoo import models, fields, api

class order(models.Model):
    _name = 'sworkshop.order'
    _description = 'Service Workshop Order'
    _order = 'id desc'
    
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle", required=True)
    opening_date = fields.Date(string="Opening Date", required=True, copy=False, default=fields.Date.today)
    mobile = fields.Char(string="Mobile")
    driver = fields.Many2one("res.partner", string="Driver", required=True)
    manager_id = fields.Many2one("res.users", string="Manager", readonly=True, index=True, tracking=True, default=lambda self: self.env.user)
    repairman_id = fields.Many2one("res.users", string="Repairman", required=True)
    helper_id = fields.Many2one("res.users", string="Helper", required=True)
    failures = fields.Char(string="Failures")
    duration = fields.Datetime(string="Duración", required=True)
    deadline = fields.Datetime(string="Deadline")
    maintenance_types_id = fields.Many2one("sworkshop.maintenance.types", string="Maintenance Types")
    driving_test = fields.Boolean(string="Driving Test")
    status = fields.Selection(string="Status", selection=[('in quotation', 'In Quotation'), ('closed', 'Closed'), ('check-in','Check-In'), ('check-out','Check-Out')], default="in quotation")

    
    