from typing import List

import uvicorn as uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
import models
from db import Session, engine

app = FastAPI()

database = Session()


class Student(BaseModel):
    id: int
    student_id: int
    student_name: str
    student_email: str
    faculty: str
    course_id: int
    group: str

    class Config:
        orm_mode = True


class Teacher(BaseModel):
    id: int
    teacher_name: str
    teacher_email: str
    department: str

    class Config:
        orm_mode = True


class Course(BaseModel):
    id: int
    course_name: str

    class Config:
        orm_mode = True


class Grade(BaseModel):
    id: int
    mark: int
    student: str
    course: str
    task: str

    class Config:
        orm_mode = True


@app.post('/students', response_model=Student, status_code=201)
def create_student(student: Student):
    new_student = models.Student(
        student_id=student.student_id,
        student_name=student.student_name,
        student_email=student.student_email,
        faculty=student.faculty,
        course=student.course_id,
        group=student.group
    )
    database.add(new_student)
    database.commit()

    return new_student


@app.get('/students/{student_id}', response_model=Student, status_code=200)
def get_student_by_student_id(student_id: int):
    return database.query(models.Student).filter(models.Student.student_id == student_id).first()


@app.put('/students/{student_id}', response_model=Student, status_code=200)
def edit_student_by_id(student_id: int, student: Student):
    student_to_edit = database.query(models.Student).filter(models.Student.student_id == student_id).first()
    student_to_edit.student_id = student.student_id
    student_to_edit.student_name = student.student_name
    student_to_edit.student_email = student.student_email
    student_to_edit.faculty = student.faculty
    student_to_edit.course = student.course_id
    student_to_edit.group = student.group

    database.commit()
    return student_to_edit


@app.delete('/students/{student_id}')
def delete_student_by_id(student_id: int):
    student_to_delete = database.query(models.Student).filter(models.Student.student_id == student_id).first()
    database.delete(student_to_delete)
    database.commit()

    return student_to_delete


@app.get('/teachers', response_model=List[Teacher], status_code=200)
def get_all_teachers():
    return database.query(models.Teacher).all()


@app.post('/courses', response_model=Course, status_code=201)
def create_course(course: Course):
    new_course = models.Course(
        course_name=course.course_name
    )
    database.add(new_course)
    database.commit()

    return new_course


@app.get('/courses/{course_id}', response_model=Course, status_code=200)
def get_course_by_id(course_id: int):
    return database.query(models.Course).filter(models.Course.id == course_id).first()


@app.get('/courses/{course_id}/students', response_model=List[Student], status_code=200)
def get_students_by_course_id(course_id: int):
    return database.query(models.Student).where(models.Student.course_id == course_id).all()


@app.post('/grades', response_model=Grade, status_code=201)
def create_grade(grade: Grade):
    new_grade = models.Grade(
        mark=grade.mark,
        student=grade.student,
        course=grade.course,
        task=grade.task
    )
    database.add(new_grade)
    database.commit()

    return new_grade


@app.put('/grades/{grade_id}', response_model=Grade, status_code=200)
def edit_grade(grade_id: int, grade: Grade):
    grade_to_edit = database.query(models.Grade).filter(models.Grade.id == grade_id).first()
    grade_to_edit.mark = grade.mark
    grade_to_edit.student = grade.student
    grade_to_edit.course = grade.course
    grade_to_edit.task = grade.task

    database.commit()
    return grade_to_edit


if __name__ == "__main__":
    models.Base.metadata.create_all(engine)
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)