# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = 'res.partner'
   
    is_instructor = fields.Boolean('Instructor?')
    session_ids = fields.Many2many('febriacademy.session', string='Sessions')
    teacher_level_id = fields.Many2one('febriacademy.teacher_level', string='Level')


