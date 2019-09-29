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

from odoo import fields, models, api, _


class EducationStudent(models.Model):
    _name = 'education.student'
    _inherit = ['mail.thread']
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Student record'
    _rec_name = 'name'


    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            recs = self.search([('name', operator, name)] + (args or []), limit=limit)
            if not recs:
                recs = self.search([('ad_no', operator, name)] + (args or []), limit=limit)
            return recs.name_get()
        return super(EducationStudent, self).name_search(name, args=args, operator=operator, limit=limit)

    @api.model
    def create(self, vals):
        """Over riding the create method to assign sequence for the newly creating the record"""
        vals['ad_no'] = self.env['ir.sequence'].next_by_code('education.student')
        res = super(EducationStudent, self).create(vals)
        return res

    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True, ondelete="cascade")
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    application_no = fields.Char(string="Application No")
    date_of_birth = fields.Date(string="Date Of birth", requird=True)
    guardian_relation = fields.Selection(
        [('father', 'Father'),('mother', 'Mother'), ('other', 'Other')],
        required=True, string="Relationship")
    guardian_name = fields.Char(string='Guardian Name')
    class_id = fields.Many2one('education.student.class', string="Class")
    admin_no = fields.Char(string="Admission Number")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              string='Gender', required=True, track_visibility='onchange')
    school_id = fields.Many2one('res.company', string='School')
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict')
    active = fields.Boolean(default=True, string="Active")


    _sql_constraints = [
        ('admin_no', 'unique(admin_no)', "Another Student already exists with this admission number!"),
    ]
