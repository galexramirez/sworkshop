# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'
    
    workshop_order_ids = fields.One2many('sworkshop.order', 'vehicle_id', string='Workshop Order')
    owner_id = fields.Many2one('res.partner', string='Owner', required=True)
    workshop_state_id = fields.Many2one('sworkshop.vehicle.state', string='State')
    serial_number = fields.Char(string='Serial Number')