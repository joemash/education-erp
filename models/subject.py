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
from odoo.exceptions import ValidationError


class EducationSubject(models.Model):
    _name = 'education.subject'

    name = fields.Char(string='Name', required=True, help="Name of the Subject")
    code = fields.Char(string="Code", required=True,  help="Enter the Subject Code")
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('code', 'unique(code)', "Subject already exists!"),
    ]



    @api.model
    def create(self, vals):
        exists = self.search([('name', '=', vals['name'])])
        if exists:
            raise ValidationError(_('The subject already exists'))
        return super(EducationSubject, self).create(vals)
