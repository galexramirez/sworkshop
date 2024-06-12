# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SworkshopVehicleState(models.Model):
    _name = 'sworkshop.vehicle.state'
    _order = 'sequence asc'
    _description = 'Workshop Vehicle Status'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()

    _sql_constraints = [('sworkshop_state_name_unique', 'unique(name)', 'State name already exists')]
