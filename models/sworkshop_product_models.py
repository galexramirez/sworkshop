# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class ProductModels(models.Model):
    _name = "sworkshop.product.models"
    _description = "Service Workshop Product Models"
    
    product_id = fields.Many2one('product.template', string='Product', required=True)
    model_id = fields.Many2one('fleet.vehicle.model', string="Model", required=True)
    brand_id = fields.Many2one("sworkshop.product.brand", string="Product Brands", related='product_id.brand_id', readonly=True)
    unique_code = fields.Char(string='Unique Code', related='product_id.unique_code', readonly=True)
    manufacturer_code = fields.Char(string='Manufacturer Code', related='product_id.manufacturer_code', readonly=True)
    application_code = fields.Char(string='Application Code', related='product_id.application_code', readonly=True)
    stamping_code = fields.Char(string='Stamping Code', related='product_id.stamping_code', readonly=True)