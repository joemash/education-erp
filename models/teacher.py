# -*- coding: utf-8 -*-
###################################################################################
#    A part of Educational ERP Project <https://www.winguerp.co.ke>
#
#    WinguInfoTech Solutions.
#    Copyright (C) 2019.
#    Author: Josephat Macharia)
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import fields, models, api


class EducationTeacher(models.Model):
    _name = 'education.teacher'
    _inherit = ['mail.thread']
    _description = 'Faculty Record'

    # @api.multi
    # def create_employee(self):
    #     """Creating the employee for the faculty"""
    #     for rec in self:
    #         values = {
    #             'name': rec.name + rec.last_name,
    #             'gender': rec.gender,
    #             'birthday': rec.date_of_birth,
    #             'image': rec.image,
    #             'work_phone': rec.phone,
    #             'work_mobile': rec.mobile,
    #             'work_email': rec.email,
    #         }
    #         emp_id = self.env['hr.employee'].create(values)
    #         rec.employee_id = emp_id.id

    @api.model
    def create(self, vals):
        """Over riding the create method to assign
        the sequence for newly creating records"""
        vals['faculty_id'] = self.env['ir.sequence'].next_by_code('education.teacher')
        res = super(EducationTeacher, self).create(vals)
        return res

    name = fields.Char(string='Name', required=True, help="Enter the first name")
    faculty_id = fields.Char(string="ID", readonly=True)
    last_name = fields.Char(string='Last Name', help="Enter the last name")
    middle_name = fields.Char(string='Middle Name', help="Enter the middle name")
    image = fields.Binary(string="Image")
    email = fields.Char(string="Email", help="Enter the Email for contact purpose")
    phone = fields.Char(string="Phone", help="Enter the Phone for contact purpose")
    date_of_birth = fields.Date(string="Date Of birth", help="Enter the DOB")
    contact_person = fields.Char(string="Full Name", help="Your contact person")
    contact_email = fields.Char(string="Email", help="Enter the Email for contact purpose")
    contact_phone = fields.Char(string="Phone", help="Enter the Phone for contact purpose")
    tsc_no = fields.Char(string="Tsc Number", help="Teacher service number")
    subject_lines = fields.Many2many('education.subject', string='Subject Lines')
    employee_id = fields.Many2one('hr.employee', string="Related Employee")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              string='Gender', required=True, default='male', track_visibility='onchange')
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict')
    active = fields.Boolean(default=True, string="Active")
    county = fields.Char(string="County")
    position = fields.Selection([
                        ('hod', 'Head of Department'),
                        ('teacher', 'Teacher'),
                        ('headmaster', 'Head Master'),
                        ('deputy headmaster', 'Deputy Head Master'),
                        ('principal', 'Principal'),
                        ('deputy principal', 'Deputy Principal'),
                        ])

    _sql_constraints = [
        ('id', 'unique(id)', "Teacher already exists!"),
    ]