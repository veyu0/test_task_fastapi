from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, unique=True)
    student_id = Column(Integer, unique=True)
    student_name = Column(String, unique=True)
    student_email = Column(String, unique=True)
    faculty = Column(String, ForeignKey('faculty.name'))
    course_id = Column(Integer, ForeignKey('course.id'))
    group = Column(String, ForeignKey('group.group_name'))

    grade = relationship('Grade')
    schedule = relationship('Schedule')
    exam = relationship('Exam')
    task = relationship('Task')


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, unique=True)
    teacher_name = Column(String, unique=True)
    teacher_email = Column(String, unique=True)
    department = Column(String, ForeignKey('department.department_name'))

    schedule = relationship('Schedule')
    building = relationship('Building')


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True, unique=True)
    course_name = Column(String, unique=True)

    student = relationship('Student')
    grade = relationship('Grade')
    schedule = relationship('Schedule')
    term = relationship('Term')
    exam = relationship('Exam')
    task = relationship('Task')
    course_program = relationship('CourseProgram')
    studying_plan = relationship('StudyingPlan')


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, unique=True)
    group_name = Column(String, unique=True)

    student = relationship('Student')


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, unique=True)
    department_name = Column(String, unique=True)

    teacher = relationship('Teacher')


class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True, unique=True)
    mark = Column(Integer)
    student = Column(String, ForeignKey('student.student_name'))
    course = Column(String, ForeignKey('course.course_name'))
    task = Column(String, ForeignKey('task.name'))


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True, unique=True)
    student = Column(String, ForeignKey('student.student_name'))
    course = Column(String, ForeignKey('course.course_name'))
    teacher = Column(String, ForeignKey('teacher.teacher_name'))


class Building(Base):
    __tablename__ = 'building'
    id = Column(Integer, primary_key=True, unique=True)
    num = Column(Integer)
    teacher = Column(String, ForeignKey('teacher.teacher_name'))
    auditorium = Column(Integer, ForeignKey('auditorium.num'))


class Auditorium(Base):
    __tablename__ = 'auditorium'
    id = Column(Integer, primary_key=True, unique=True)
    num = Column(Integer, unique=True)

    building = relationship('Building')


class Term(Base):
    __tablename__ = 'term'
    id = Column(Integer, primary_key=True, unique=True)
    num = Column(Integer)
    course = Column(String, ForeignKey('course.course_name'))


class Faculty(Base):
    __tablename__ = 'faculty'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, unique=True)

    student = relationship("Student")


class Exam(Base):
    __tablename__ = 'exam'
    id = Column(Integer, primary_key=True, unique=True)
    type = Column(String)
    course = Column(String, ForeignKey('course.course_name'))
    student = Column(String, ForeignKey('student.student_name'))


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, unique=True)
    course = Column(String, ForeignKey('course.course_name'))
    student = Column(String, ForeignKey('student.student_name'))
    date = Column(Date)

    grade = relationship('Grade')


class CourseProgram(Base):
    __tablename__ = 'course_program'
    id = Column(Integer, primary_key=True, unique=True)
    course = Column(String, ForeignKey('course.course_name'))
    lesson = Column(String)


class StudyingPlan(Base):
    __tablename__ = 'studying_plan'
    id = Column(Integer, primary_key=True, unique=True)
    course = Column(String, ForeignKey('course.course_name'))
    date_od_course = Column(Date)