# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class MaintenanceTypes(models.Model):
    _name = "sworkshop.maintenance.types"
    _description = "Maintenance Types"
    
    name = fields.Char(string="Maintenance Types", required=True)