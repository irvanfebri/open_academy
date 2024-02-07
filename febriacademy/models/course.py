# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'febriacademy.febriacademy'
    _description = 'febriacademy.febriacademy'

    _sql_constraints = [
        ('_check_name_unique', 'UNIQUE(name)', 'Name must be unique'),
        ('_check_name_different_description', 'CHECK(name != description)', 'Name and description must be different'),
    ]

    name = fields.Char(string="Name")
    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('febriacademy.session', 'course_id', string='Sessions')
    description = fields.Text(string="Description")

    def copy(self, default=None):
        default = dict(default or {})
    
        copied_count = self.search_count(
            [('name', '=like','copy of {}%'.format(self.name))])

        #training odoo 
        #copy data

        #kalo ada 
        if not copied_count:
            new_name = "Copy of {}".format(self.name)

        #kalo tidak ada
        else: 
            new_name = "Copy of {} ({})".format(self.name, copied_count)
    
        default['name'] = new_name
        return super (Course, self).copy(default)