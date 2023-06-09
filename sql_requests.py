from db import Session

from models import Base, Student, Course, Faculty, Group, Grade, Task, Teacher, Department, Auditorium, Building, Term

session = Session()
# Insertion of data
math = Course(
    id=1,
    course_name='Math'
)

faculty = Faculty(
    name='Computer Science'
)

group = Group(
    group_name='CS0001'
)

gamlet = Student(
    student_id=1,
    student_name='Karapetyan Gamlet',
    student_email='test1@gmail.com',
    faculty='Computer Science',
    course_id='1',
    group='CS0001'
)

faith = Student(
    student_id=2,
    student_name='Karapetyan Faith',
    student_email='test2@gmail.com',
    faculty='Computer Science',
    course_id='1',
    group='CS0001'
)

task = Task(
    name='Written Assignment',
    course='Math',
    student='Karapetyan Faith',
    date='01.01.2019'
)

grade = Grade(
    mark=100,
    student='Karapetyan Faith',
    course='Math',
    task='Written Assignment'
)

department = Department(
    department_name='University of the People'
)
teacher1 = Teacher(
    teacher_name='Tony Montana',
    teacher_email='tony1@gmail.com',
    department='University of the People'
)
teacher2 = Teacher(
    teacher_name='Lana Walter',
    teacher_email='lana_w@gmail.com',
    department='University of the People'
)

aud_101 = Auditorium(
    num=101
)
aud_303 = Auditorium(
    num=303
)
building = Building(
    num=3,
    teacher='Tony Montana',
    auditorium=303
)

session.add_all([math, group, faculty, gamlet, faith, task, grade,
                 department, teacher1, teacher2, aud_101, aud_303, building])
session.commit()

# SQL requests
# Выбрать всех студентов, обучающихся на курсе "Математика"
math_sql = session.query(Student).where(Student.course_id == 1)
math_students_list = [student.student_name for student in math_sql]

# Обновить оценку студента по курсу.
grade_query = session.query(Grade)
clean_py_query = grade_query.filter(Grade.student == 'Karapetyan Faith')
clean_py_query.update({Grade.mark: 99})

# Выбрать всех преподавателей, которые преподают в здании №3
building_sql = session.query(Building).where(Building.num == 3)
building_teachers_list = [b.teacher for b in building_sql]

# Удалить задание для самостоятельной работы, которое было создано более года назад
task_query = session.query(Task)
grade_to_delete = 'Written Assignment'
session.query(Grade).filter(Grade.task == grade_to_delete).delete()
clean_py_query = task_query.filter(Task.date <= '01.01.2023')
clean_py_query.delete()

# Добавить новый семестр в учебный год
sql_add_term = Term(
    num=4,
    course='Math'
)
session.add(sql_add_term)
session.commit()
