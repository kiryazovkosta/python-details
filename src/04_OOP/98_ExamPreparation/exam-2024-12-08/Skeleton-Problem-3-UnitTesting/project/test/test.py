from project.senior_student import SeniorStudent

from unittest import TestCase

class TestSeniorStudent(TestCase):

    def setUp(self):
        self.senior_student = SeniorStudent("1234", "Student", 5.00)

    def test_SeniorStudent_init(self):
        self.assertEqual("1234", self.senior_student.student_id)
        self.assertEqual("Student", self.senior_student.name)
        self.assertEqual(5.00, self.senior_student.student_gpa)

    def test_SeniorStudent_student_id_raises(self):
        invalid_ids = ["", "1", "12", "123", "    ", "  1  "]
        for invalid_id in invalid_ids:
            with self.assertRaises(ValueError) as ex:
                self.senior_student.student_id = invalid_id
            self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_SeniorStudent_name_raises(self):
        invalid_names = ["", " "]
        for invalid_name in invalid_names:
            with self.assertRaises(ValueError) as ex:
                self.senior_student.name = invalid_name
            self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_SeniorStudent_student_gpa_raises(self):
        invalid_gpas = [-1, -0.01, 0, 0.9, 1.0]
        for invalid_gpa in invalid_gpas:
            with self.assertRaises(ValueError) as ex:
                self.senior_student.student_gpa = invalid_gpa
            self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_SeniorStudent_apply_to_college_return_error(self):
        self.assertEqual(0, len(self.senior_student.colleges))
        self.senior_student.colleges.add("one")
        self.assertEqual(1, len(self.senior_student.colleges))
        result = self.senior_student.apply_to_college(6.00, "college")
        self.assertEqual('Application failed!', result)
        self.assertEqual(1, len(self.senior_student.colleges))

    def test_SeniorStudent_apply_to_college_successfully(self):
        self.assertEqual(0, len(self.senior_student.colleges))
        self.senior_student.colleges.add("one")
        self.assertEqual(1, len(self.senior_student.colleges))
        result = self.senior_student.apply_to_college(4.00, "college")
        self.assertEqual('Student successfully applied to college.', result)
        self.assertEqual(2, len(self.senior_student.colleges))
        self.assertIn("one", self.senior_student.colleges)
        self.assertIn("college".upper(), self.senior_student.colleges)

    def test_SeniorStudent_update_gpa_equal_to_one_return_error(self):
        result = self.senior_student.update_gpa(1.00)
        self.assertEqual('The GPA has not been changed!', result)
        self.assertEqual(5.00, self.senior_student.student_gpa)

    def test_SeniorStudent_update_gpa_smaller_than_one_return_error(self):
        result = self.senior_student.update_gpa(-0.50)
        self.assertEqual('The GPA has not been changed!', result)
        self.assertEqual(5.00, self.senior_student.student_gpa)

    def test_SeniorStudent_update_gpa_bigger_than_one_return_success(self):
        result = self.senior_student.update_gpa(6.00)
        self.assertEqual('Student GPA was successfully updated.', result)
        self.assertEqual(6.00, self.senior_student.student_gpa)

    def test_SeniorStudent_eq(self):
        other = SeniorStudent("2345", "Other", 1.01)
        values = {
            1.01: False,
            2.0: False,
            5.0: True,
            6.0: False
        }

        for key, value in values.items():
            other.student_gpa = key
            result = self.senior_student == other
            self.assertEqual(value, result)



