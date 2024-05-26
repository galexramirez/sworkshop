# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Order(models.Model):
    _name = 'sworkshop.order'
    _description = 'Workshop Order'
    _order = 'id desc'
    
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle", required=True)
    opening_date = fields.Date(string="Opening Date", required=True, copy=False, default=fields.Date.today)

