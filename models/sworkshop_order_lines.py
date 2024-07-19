# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class OrderLines(models.Model):
    _name = "sworkshop.order.lines"
    _description = "Service Workshop Order Lines"
    _order = "product_id desc"
    
    product_id = fields.Many2one('product.template', string="Product", required=True)
    order_id = fields.Many2one('sworkshop.order', string='Order', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    
