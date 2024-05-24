# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Order(models.Model):
    _name = 'repair.order'
    _description = 'Repair Order'
    _order = 'id desc'
    
    customer = fields.Many2one("res.partner", string="Customer", required=True)
    vehicle = fields.Many2one("fleet.vehicle", string="Vehicle", required=True)
    opening_date = fields.Date(string="Date", string="Opening Date", required=True, copy=False, default=fields.Date.today)

