# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class OrderLine(models.Model):
    _name = "sworkshop.order.line"
    _description = "Service Workshop Order Line"
    
    company_id = fields.Many2one(
        related='order_id.company_id',
        store=True, index=True, precompute=True)
    
    product_id = fields.Many2one('product.template', string="Product", required=True)
    brand_id = fields.Many2one("sworkshop.product.brand", string="Product Brands", related='product_id.brand_id', readonly=True)
    unique_code = fields.Char(string='Unique Code', related='product_id.unique_code', readonly=True)
    manufacturer_code = fields.Char(string='Manufacturer Code', related='product_id.manufacturer_code', readonly=True)
    application_code = fields.Char(string='Application Code', related='product_id.application_code', readonly=True)
    stamping_code = fields.Char(string='Stamping Code', related='product_id.stamping_code', readonly=True)
    order_id = fields.Many2one('sworkshop.order', string='Order', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    model_id = fields.Many2one("fleet.vehicle.model", string="Vehicle Model", related="order_id.model_id")
    
    @api.model
    def create(self, vals):
        self.env['sworkshop.order'].browse(vals['order_id']).update({'state':'check_out'})
        return super(OrderLine, self).create(vals)    