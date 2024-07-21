# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class ProductBrand(models.Model):
    _name = "sworkshop.product.brand"
    _description = "Product Brands"
    
    name = fields.Char(string="Product Brands", required=True)