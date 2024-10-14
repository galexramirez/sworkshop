# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class Technical(models.Model):
    _inherit = 'res.users'
    
    vehicle_models = fields.Many2many('fleet.vehicle.model', 
                                         relation='technical_vehicle_model',
                                         column1="technical_id",
                                         column2='vehicle_model_id')
    sworkshop_order_ids = fields.One2many("sworkshop.order", "repairman_id", string="SW Order")
    is_technical = fields.Boolean(string="Is Technical")