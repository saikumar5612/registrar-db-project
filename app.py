# app.py
from flask import Flask, render_template, abort
import models

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="Welcome to the Registrar's Database")

# Student routes
@app.route('/students/all')
def students_all():
    students = models.get_students()
    return render_template('students.html', students=students)

@app.route('/students/<int:student_number>')
def student_detail(student_number):
    student = models.get_student_by_number(student_number)
    grades = models.get_student_grades(student_number)

    if student is None:
        return abort(404)  # Return a 404 error if student is not found

    return render_template('student_detail.html', student=student, grades=grades)

# Instructor routes
@app.route('/instructors/<string:instructor_name>')
def instructor_detail(instructor_name):
    instructor_courses = models.get_instructor_courses(instructor_name)
    return render_template('instructors.html', instructor=instructor_name, courses=instructor_courses)

# Course routes
@app.route('/courses/all')
def courses_all():
    courses = models.get_courses()
    return render_template('courses.html', courses=courses)

@app.route('/courses/<string:course_number>')
def course_detail(course_number):
    course = models.get_course_by_number(course_number)
    prerequisites = models.get_prerequisites(course_number)

    if course is None:
        return abort(404)  # Return a 404 error if course is not found

    return render_template('course_detail.html', course=course, prerequisites=prerequisites)

if __name__ == '__main__':
    app.run(debug=True)
