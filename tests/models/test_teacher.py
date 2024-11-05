import pytest
from datetime import date
from models.teacher import Teacher, Course

def test_create_teacher():
    teacher = Teacher(first_name="Jane", last_name= "Doe", age=30, hiring_date=date(2020, 1, 1))
    assert teacher.first_name == "Jane"
    assert teacher.last_name == "Doe"
    assert teacher.age == 30
    assert teacher.hiring_date == date(2020, 1, 1)
    assert teacher.courses_teached == []