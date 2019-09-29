from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class StudentResult(models.Model):
    _name = 'education.student.result'

    date = fields.Date(
        string='Date',
        default=lambda self:fields.Date.today()
    )
    student = fields.Many2one(
        'education.student',
        string='Student',
        required=True
    )
    class_id = fields.Many2one(
        'education.student.class',
        string='Class',
        required=True

    )
    term = fields.Selection(
          [
         ('Term 1', 'Term 1'),
         ('Term 2', 'Term 2'),
         ('Term 3', 'Term 3')
        ],
        string='Term',
        required=True
    )
    subject_line = fields.One2many(
        'education.student.result.lines',
        'result_id',
        string='Student Lines'
    )
    total_mark_scored = fields.Float(string='Total Marks Scored', store=True, readonly=True, compute='_total_marks_all')

    @api.depends('subject_line.mark_scored')
    def _total_marks_all(self):
        for results in self:
            total_mark_scored = 0
            for subjects in results.subject_line:
                total_mark_scored += subjects.mark_scored
            results.total_mark_scored = total_mark_scored
    

class StudentResultLines(models.Model):
    _name = 'education.student.result.lines'

    result_id = fields.Many2one(
        'education.student.result',
        string='Student Result Id'
    )
    subject = fields.Many2one(
        'education.subject',
        string='Subject',
        required=True
    )
    mark_scored = fields.Float(
        string='Marks Scored',
        required=True
    )
    grade = fields.Selection(
          [
         ('A', 'A'),
         ('A-', 'A-'),
         ('B+', 'B+'),
         ('B', 'B'),
         ('B-', 'B-'),
         ('C+', 'C+'),
         ('C', 'C'),
         ('C-', 'C-'),
         ('D+', 'D+'),
         ('D', 'D'),
         ('D-', 'D-'),
         ('E', 'E'),
        ],
        string='Grade',
        required=True
    )
    comments = fields.Text(string='Comments')


    @api.onchange('mark_scored')
    def check_mark_scored(self):
        for record in self:
            if record.mark_scored < 0 or record.mark_scored > 100:
                raise ValidationError(_('Marks scored should be between 0 and 100'))
