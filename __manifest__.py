# -*- coding: utf-8 -*-
###################################################################################
#    A part of Elimu ERP Project <https://www.winguerp.co.ke>
#
#    WinguInfoTech Solutions.
#    Copyright (C) 2019 (<https://www.cybrosys.com>).
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
{
    'name': 'Elimu ERP Core',
    'version': '12.0.1.0.1',
    'summary': """Core Module of Elimu ERP""",
    'description': 'Core Module of Elimu ERP',
    'category': 'Educational',
    'author': 'WinguInfoTech Solutions',
    'company': 'WinguInfoTech Solutions',
    'website': "http://www.winguerp.co.ke",
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/class.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/sequence.xml',
        'views/subject.xml',
        'views/attendance.xml',
        'views/student_result.xml',
        'views/promote_student.xml',
        'views/main_menu.xml',
        'report/student_report_menu.xml',
        'report/student_report_template.xml',
        'report/student_attendance_menu.xml',
        'report/student_attendance_report_template.xml',
    ],
    'demo': [
        'demo/data.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
