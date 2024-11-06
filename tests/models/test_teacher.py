import pytest
from datetime import date
from models.teacher import Teacher
from models.course import Course
from models.student import Student

def test_create_teacher():
    teacher = Teacher(first_name="Jane", last_name= "Doe", age=30, hiring_date=date(2020, 1, 1))
    assert teacher.first_name == "Jane"
    assert teacher.last_name == "Doe"
    assert teacher.age == 30
    assert teacher.hiring_date == date(2020, 1, 1)
    assert teacher.courses_teached == []

def test_add_course():
    student = Student(first_name="John", last_name="Doe", age=20)
    course = Course(name="Math 101", start_date=date(2024, 1, 1), end_date=date(2024, 6, 1))
    student.add_course(course)
    assert course in student.courses_taken
