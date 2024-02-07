# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TeacherLevel(models.Model):
    _name = 'febriacademy.teacher_level'
    _description = 'febriacademy.teacher_level'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")


