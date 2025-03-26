from unittest import TestCase
from project.student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("StudentName", {"course1": [1, 3]})

    def test_student_init(self):
        self.assertEqual("StudentName", self.student.name)
        self.assertDictEqual({"course1": [1, 3]}, self.student.courses)

    def test_student_init_non_empty(self):
        temp_student = Student("Name")
        self.assertEqual("Name", temp_student.name)
        self.assertDictEqual({}, temp_student.courses)

    def test_student_add_notes_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("non_exists", [1, 2, 3])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_student_add_notes(self):
        result = self.student.add_notes("course1", 2)
        self.assertEqual("Notes have been updated", result)
        self.assertListEqual([1, 3, 2], self.student.courses["course1"])

    def test_student_leave_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("non_exists")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_student_leave_course(self):
        result = self.student.leave_course("course1")
        self.assertEqual("Course has been removed", result)

    def test_student_enroll_already_added(self):
        result = self.student.enroll("course1", [1, 2])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_student_enroll_notes_empty(self):
        result = self.student.enroll("new course", [1, 2])
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_enroll_notes_yes(self):
        result = self.student.enroll("new course", [1, 2], "Y")
        self.assertEqual("Course and course notes have been added.", result)

    def test_student_enroll_notes_added(self):
        result = self.student.enroll("new course", [1, 2], "N")
        self.assertEqual("Course has been added.", result)





