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

from odoo.exceptions import ValidationError
from odoo import fields, models, api, _


class EducationStudentClass(models.Model):
    _name = 'education.student.class'
    _description = "Class room"


    name = fields.Selection(
        [
          ('1', '1'),('2', '2'), ('3', '3'),
          ('4', '4'), ('5', '5'), ('6', '6'),
          ('7', '7'), ('8', '8')
        ],string='Name', required=True)
    student_count = fields.Integer(string='Students Count', compute='_get_student_count')


    @api.model
    def create(self, vals):
        exists = self.search([('name', '=', vals['name'])])
        if exists:
            raise ValidationError(_('The student class already exists'))
        return super(EducationStudentClass, self).create(vals)


    @api.multi
    def view_students(self):
        """Return the list of current students in this class"""
        self.ensure_one()
        students = self.env['education.student'].search([('class_id', '=', self.id)])
        students_list = students.mapped('id')
        return {
            'domain': [('id', 'in', students_list)],
            'name': _('Students'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'education.student',
            'view_id': False,
            'context': {'default_class_id': self.id},
            'type': 'ir.actions.act_window'
        }

    def _get_student_count(self):
        """Return the number of students in the class"""
        for rec in self:
            students = self.env['education.student'].search([('class_id', '=', rec.id)])
            student_count = len(students) if students else 0
            rec.update({
                'student_count': student_count
            })
