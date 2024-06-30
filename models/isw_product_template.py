# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    brand = fields.Char(string='Brand')
    unique_code = fields.Char(string='Unique Code')
    manufacturer_code = fields.Char(string='Manufacturer Code')
    application_code = fields.Char(string='Application Code')
    stamping_code = fields.Char(string='Stamping Code')

