# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class ProductModels(models.Model):
    _name = "sworkshop.product.models"
    _description = "Service Workshop Product Models"
    _order = "model_id asc"
    
    model_id = fields.Many2one('fleet.vehicle.model', string="Model", required=True)
    product_id = fields.Many2one('product.template', string='Product', required=True)
    
