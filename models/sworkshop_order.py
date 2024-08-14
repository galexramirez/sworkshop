# -*- coding: utf-8 -*-

from odoo import models, fields, api

class order(models.Model):
    _name = 'sworkshop.order'
    _description = 'Service Workshop Order'
    _order = 'id desc'
    
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    owner_id = fields.Many2one("res.partner", string="Owner", required=True, related="customer_id", readonly=False)
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle", required=True, 
    domain=[('owner_id','=',owner_id)]
    )
    opening_date = fields.Date(string="Opening Date", required=True, copy=False, default=fields.Date.today)
    mobile = fields.Char(string="Mobile", related="customer_id.mobile", readonly=False)
    driver = fields.Many2one("res.partner", string="Driver")
    manager_id = fields.Many2one("res.users", string="Manager", index=True, tracking=True, default=lambda self: self.env.user)
    repairman_id = fields.Many2one("res.users", string="Repairman", required=True)
    helper_id = fields.Many2one("res.users", string="Helper", required=True)
    failures = fields.Text(string="Failures")
    duration = fields.Datetime(string="Duration", required=True)
    deadline = fields.Datetime(string="Deadline")
    maintenance_types_id = fields.Many2one("sworkshop.maintenance.types", string="Maintenance Types")
    driving_test = fields.Boolean(string="Driving Test")
    status = fields.Selection(string="Status", selection=[('check-in','Check-In'), ('check-out','Check-Out'), ('in-quotation', 'In Quotation'), ('closed', 'Closed'), ('canceled','Canceled')], default="check-in")
    lines_ids = fields.One2many("sworkshop.order.lines", "order_id", string="Order Lines")
    to_repair = fields.Text(string="To Repair")
    model_id = fields.Many2one("fleet.vehicle.model", string="Vehicle Model", related="vehicle_id.model_id")
    
    """ @api.onchange('owner_id')
    def _onchange_owner_id(self):
        domain = {'vehicle_id': [('owner_id', '=', self.owner_id)]}
        return {'domain': domain} """