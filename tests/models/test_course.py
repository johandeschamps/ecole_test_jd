import pytest
from datetime import date
from models.course import Course
from models.student import Student
from models.teacher import Teacher


def test_add_student():
    course = Course(name="Math 101", start_date=date(2024, 1, 1), end_date=date(2024, 6, 1))
    student = Student(first_name="John", last_name= "Doe", age=20)
    course.add_student(student)
    assert student in course.students_taking_it
    assert course in student.courses_taken

def test_set_teacher():
    course = Course(name="Math 101", start_date=date(2024, 1, 1), end_date=date(2024, 6, 1))
    teacher = Teacher(first_name="Jane", last_name="Doe", age=30, hiring_date=date(2020, 1, 1))
    course.set_teacher(teacher)
    assert course.teacher == teacher
    assert course in teacher.courses_teached
