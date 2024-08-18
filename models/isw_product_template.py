# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    brand_id = fields.Many2one("sworkshop.product.brand", string="Product Brands")
    unique_code = fields.Char(string='Unique Code')
    manufacturer_code = fields.Char(string='Manufacturer Code')
    application_code = fields.Char(string='Application Code')
    stamping_code = fields.Char(string='Stamping Code')
    models_ids = fields.One2many("sworkshop.product.models", "product_id", string="Product Models")
    model_id = fields.Many2one("fleet.vehicle.model", string="Vehicle Model", related="models_ids.model_id")