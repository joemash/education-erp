from odoo import models, fields, api, _
from datetime import date, datetime
from odoo.exceptions import except_orm


class PromoteStudent(models.Model):
    _name = "education.promote.student"

    name = fields.Char(default='Student')
    class_id = fields.Many2one('education.student.class', string="Class")
    promote_to_class = fields.Many2one('education.student.class', string="Promote To Class")
    student_list = fields.Boolean('Student List')
    student_line = fields.One2many('education.promote.student.line', 'promote_student_id', 'Promoted Students')

    @api.onchange('class_id')
    def onchange_class(self):
        class_obj = self.env['education.student.class']
        if self.class_id:
            if self.class_id.is_last_class:
                raise except_orm(_('Warning!'), _("You cannot proceed with promotion process for %s!")
                                 %self.class_id.name)
            if not self.class_id.is_last_class and not self.class_id.next_class:
                raise except_orm(_('Warning!'), _("Next class is not defined!"))
            self.promote_to_class = self.class_id.next_class.id
            
  
    @api.model
    def create(self, vals):
        class_obj = self.env['education.student.class']
        class_brw = class_obj.browse(vals['class_id'])
        if 'class_id' in vals and 'promote_to_class' in vals:
            if vals['class_id'] and vals['promote_to_class']:
                if class_brw.is_last_class:
                    raise except_orm(_('Warning!'), _("You cannot proceed with promotion process for %s!")%class_brw.name)
                if not class_brw.next_class:
                    raise except_orm(_('Warning!'), _("Next class is not defined!"))
                if class_obj.browse(vals['promote_to_class']).id != class_brw.next_class.id:
                    raise except_orm(_('Warning!'),
                        _("promote to class can not be equal to or lower than current class!!"))
        return super(PromoteStudent, self).create(vals)


    @api.multi
    def write(self, vals):
        class_obj = self.env['education.student.class']
        if 'class_id' in vals or 'promote_to_class' in vals:
            if 'class_id' not in vals:  
                vals['class_id']=self.class_id.id
            if 'promote_to_class'not in vals:
                vals['promote_to_class'] = self.promote_to_class.id
                
            if vals['class_id'] or vals['promote_to_class']:
                class_brw = class_obj.browse(vals['class_id'])
                if class_brw.is_last_class:
                    raise except_orm(_('Warning!'), _("You cannot proceed with promotion process for %s!") % class_brw.name)
                if not class_brw.next_class:
                    raise except_orm(_('Warning!'), _("Next class is not defined!"))
                # if class_obj.browse(vals['promote_to_class']).name != class_brw.next_class:
                #     raise except_orm(_('Warning!'), _("Promote to class can not be equal to or lower than current class!!"))
        return super(PromoteStudent, self).write(vals)
    
    @api.multi
    def show_student_list(self):
        student_obj = self.env['education.student']
        student_promote_lines_obj = self.env['education.promote.student.line']
        student_data = student_obj.search([('class_id', '=', self.class_id.id)])
        if not student_data:
            raise except_orm(_('Warning!'), _("There are no students to promote."))
        for student in student_data:
            lines = {
                'promote_student_id': self.ids[0],
                'student_id': student.id,
                'current_academic_class': student.class_id.id,
                'new_acad_class': self.promote_to_class.id,
            }
            student_promote_lines_obj.create(lines)


    @api.multi
    def student_promotion(self):
        if not self.promote_to_class:
            raise except_orm(_('Warning!'), _("The next class is not defined."))
        for student in self.student_line:
            if student.state == 'draft':
                student.student_id.promoted = True
                student.student_id.class_id = student.new_acad_class 
                student.state = 'promote'


class PromoteStudentLine(models.Model):

    _name = "education.promote.student.line"

    student_id = fields.Many2one('education.student', 'Student')
    current_academic_class = fields.Many2one('education.student.class', 'Current Class')
    new_acad_class = fields.Many2one('education.student.class', 'New Class')
    promote_student_id = fields.Many2one('education.promote.student', 'Student Reference')
    state = fields.Selection([('draft', 'Draft'), ('promote', 'Promoted')],
                             string='State', default='draft')

    @api.multi
    def unlink(self):
        for student in self:
            if student.state == 'promote':
                raise except_orm(_('Warning!'),_("You can not delete this record"))
        return super(PromoteStudentLine, self).unlink()

    
class StudentClassInherit(models.Model):
    _inherit = 'education.student.class'

    next_class = fields.Many2one('education.student.class', 'Next Class')
    is_last_class = fields.Boolean('Last Class')

    #TODO validate next_class to be unique 


class StudentPromotion(models.Model):
    _inherit = 'education.student'

    promoted = fields.Boolean(string='Promoted')
