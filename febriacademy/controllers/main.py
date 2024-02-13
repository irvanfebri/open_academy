# -*- coding: utf-8 -*-
from odoo import http

class febriacademy(http.Controller):

    @http.route('/febriacademy', auth='public')
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/febriacademy/template/', auth='public')
    def template(self, **kw):
        return http.request.render('febriacademy.template', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })

    @http.route('/febriacademy/data', auth='public')
    def data(self, **kw):
        Courses = http.request.env['febriacademy.febriacademy'].sudo().search([])
        return http.request.render('febriacademy.data', {
            'courses': Courses,
        })
    
    @http.route('/first-route/<name>', auth="public", website=True)
    def first_route(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/second-route/<int:id>', auth="public", website=True)
    def second_route(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/course/<model("febriacademy.febriacademy"):course>/', auth='public', website=True)
    def detail_course(self, course):
        return http.request.render('febriacademy.detail_course', {
            'course' : course
        })

    @http.route('/course', auth='public', website=True)
    def course(self, **kw):
        Courses = http.request.env['febriacademy.febriacademy']
        return http.request.render('febriacademy.course', {
            'courses': Courses.sudo().search([])
        })
    
    # Add Course 
    @http.route('/febriacademy/add_course', auth='public', website=True)
    def add_course(self, **kw):
        user_ids = http.request.env['res.users'].sudo().search([])
        return http.request.render('febriacademy.add_course', {
            'users':user_ids
        })
    
    @http.route('/febriacademy/do_add_course', auth='public', methods=['POST'], website=True)
    def do_add_course(self, **post): 
        vals = { 
            'name': post.get('name'), 
            'user_id': int(post,get('user_id')),
            'description':post.get('description'),
        }
        http.request.env['febriacademy.febriacademy'].sudo().create(vals)
        return http.request.redirect('/course')
    
