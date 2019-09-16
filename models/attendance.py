from odoo import fields, api, models


class StudentAttendance(models.Model):
    _name = 'education.attendance'
    _inherit = ['mail.thread']

    date = fields.Date(
        string='Date',
        default=lambda self:fields.Date.today()
    )
    class_id = fields.Many2one('education.student.class', string='Class')
    
    term = fields.Selection(
        [
         ('Term 1', 'Term 1'),
         ('Term 2', 'Term 2'),
         ('Term 3', 'Term 3')
        ],
        string='Term',
        required=True
    )
    attendance_id = fields.One2many(
        'education.attendance.lines',
        'attendance',
        string='Attendance_ids'
    )

    # TODO: On change of class_id populate respective students
    # @api.onchange('class_id')
    # def onchange_class_id(self):
    #     for line in self.attendance_id:
    #         line.student = self.env['education.student'].search([('class_id', '=', self.class_id)])


class StudentAttendanceLine(models.Model):
    _name = 'education.attendance.lines'
    _inherit = ['mail.thread']

    student = fields.Many2one(
        'education.student',
        string='Student'
    )
    attendance = fields.Many2one(
        'education.attendance',
         string='Attendance'
    )
    status = fields.Selection(
        [
            ('absent', 'Absent'),
            ('present', 'Present'),
        ],
        string='Status',
        required=True
    )
