from odoo import models, api


class StudentResultReport(models.AbstractModel):
    _name = 'student_result_report'
    _description = 'Student Result Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        docargs = {
            'doc_ids': docids,
            'doc_model': model,
            'data': data,
            'docs': docs,
        }
        return docargs


