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
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None, order=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', '|', '|', '|', ('name', operator, name), ('brand_id', operator, name), ('unique_code', operator, name), ('manufacturer_code', operator, name), ('application_code', operator, name), ('stamping_code', operator, name) ]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid, order=order)    
    
    