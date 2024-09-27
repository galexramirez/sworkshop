# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class FleetVehicleModel(models.Model):
    _inherit = 'fleet.vehicle.model'
    
    product_id = fields.Many2one('product.template', string='Product', required=True)
    products_ids = fields.One2many("sworkshop.product.models", "model_id", string="Model Products")
    technical_sheet = fields.Html(string='Technical Sheet')
    vehicle_type = fields.Selection(selection_add=[('motor','Motor')], ondelete={'motor':'cascade'})
    