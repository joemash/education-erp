import time 

from odoo.tests import TransactionCase, tagged


@tagged('-standard', 'nice')
class StudentTest(TransactionCase):
    def setUp(self):
        super(StudentTest, self).setUp()
        partner_id = self.env.ref("base.res_partner_2")
        student_model = self.env['education.student']
        guardian_names = self.env['res.partner'].create({
            'name': 'Partner'
        })#search([('user_ids', '=', self.env.ref('education.student').id)], limit=1)
        class_id = self.env['education.student.class'].create({
          'name': 'One'  
        })#search([()], limit=1)

        school = self.env['res.company'].create({
            'name': 'My Company'
        })


    def test_student_create(self):
        self.student_model.create({
            'partner_id': self.partner_id.id,
            'middle_name': 'Jina',
            'last_name': 'Mwisho',
            'application_no': 'K155',
            'date_of_birth': time.strftime('%Y') + '-07-15',
            'guardian_name': self.guardian_names.id,
            'father_name': 'Baba',
            'mother_name': 'Mam',
            'class_id': self.class_id.id,
            'admin_no': 'Mn105',
            'gender': 'Male',
            'school_id': self.school.id,
            'nationality': 'Kenya'
        })
        import pdb;pdb.set_trace()
