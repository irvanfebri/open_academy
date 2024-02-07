# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'febriacademy.session'
    _description = 'febriacademy.session'

    name = fields.Char(string="Name")
    partner_ids = fields.Many2many('res.partner', string='Attendees')
    course_id = fields.Many2one('febriacademy.febriacademy', string='Course')
    partner_id = fields.Many2one('res.partner', string='Instructor', domain="['|',('is_instructor','=',True),('teacher_level_id','!=', False)]")
    start_date = fields.Date(string="Start Date")
    duration = fields.Float(string="Duration")
    number_of_seats = fields.Float(string='Number Of Seats')
    description = fields.Text(string="Description")
    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats')
    active = fields.Boolean('active', default=True)
    number_of_attendees = fields.Float(compute='_compute_number_of_attendees', string='Number Of Attendees', store=True)
    
    @api.depends('partner_ids')
    def _compute_number_of_attendees(self):
        for rec in self:
            rec.number_of_attendees = len(rec.partner_ids) 
            

    @api.depends('number_of_seats','partner_ids')
    def _compute_taken_seats(self):
        for rec in self:
            if rec.partner_ids:
                rec.taken_seats = len(rec.partner_ids) /  rec.number_of_seats * 100 
            else:
                rec.taken_seats = 0

    # onchange handler
    @api.onchange('number_of_seats', 'partner_ids')
    def _onchange_number_of_seats_or_partner_ids(self):
        if self.number_of_seats < 0:
            return {
            'warning': {
                'title': "Invalid values",
                'message': "Cannot input negatif number on setas",
        }
    }

        if len(self.partner_ids) > self.number_of_seats :
            return {
            'warning': {
                'title': "Something be habpper",
                'message': "Participants Cannot input negatif number on setas",
        }
    }




    @api.constrains('partner_id','partner_ids')
    def _check_something(self):
        for record in self:
            if record.partner_id in record.partner_ids:
                raise ValidationError("Instructir Cannot be attendees: %s" % record.partner_id.name)
    # all records passed the test, don't return anything



    


