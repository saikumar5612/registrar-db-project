from mysql.connector import connect, Error

# Function to connect to the database
def get_db_connection():
    try:
        conn = connect(
            host='localhost',  # Replace with your host, e.g. '127.0.0.1'
            user='root',  # Replace with your database username
            password='sai1234',  # Replace with your database password
            database='registrar_db'  # Replace with your database name
        )
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None  # Return None if connection fails

def get_students():
    conn = get_db_connection()
    if conn is None:
        return []  # Return an empty list if connection fails

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM STUDENT")
    students = cursor.fetchall()
    conn.close()
    return students

def get_student_by_number(student_number):
    conn = get_db_connection()
    if conn is None:
        return None  # Return None if connection fails

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM STUDENT WHERE Student_number = %s", (student_number,))
    student = cursor.fetchone()
    conn.close()
    return student

def get_student_grades(student_number):
    conn = get_db_connection()  # Ensure this returns a valid connection
    if conn is None:
        return []  # Return an empty list if connection fails

    cursor = conn.cursor(dictionary=True)
    query = '''
    SELECT c.course_name, c.course_number, g.grade
    FROM GRADE_REPORT g
    JOIN SECTION s ON g.Section_identifier = s.Section_identifier
    JOIN COURSE c ON s.course_number = c.course_number
    WHERE g.Student_number = %s
    '''
    try:
        cursor.execute(query, (student_number,))
        grades = cursor.fetchall()  # Ensure this returns expected results
    except Exception as e:
        print(f"Error fetching grades: {e}")
        grades = []
    finally:
        cursor.close()
        conn.close()

    return grades

def get_instructor_courses(instructor_name):
    conn = get_db_connection()
    if conn is None:
        return []  # Return an empty list if connection fails

    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT COURSE.course_name, SECTION.Semester, SECTION.Year 
        FROM SECTION
        JOIN COURSE ON SECTION.course_number = COURSE.course_number
        WHERE SECTION.Instructor = %s
    """, (instructor_name,))
    courses = cursor.fetchall()
    conn.close()
    return courses

def get_courses():
    conn = get_db_connection()
    if conn is None:
        return []  # Return an empty list if connection fails

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM COURSE")
    courses = cursor.fetchall()
    conn.close()
    return courses

def get_course_by_number(course_number):
    conn = get_db_connection()
    if conn is None:
        return None  # Return None if connection fails

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM COURSE WHERE course_number = %s", (course_number,))
    course = cursor.fetchone()
    conn.close()
    return course

def get_prerequisites(course_number):
    conn = get_db_connection()
    if conn is None:
        return []  # Return an empty list if connection fails

    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT PREREQUISITE.Prerequisite_number, COURSE.course_name AS prerequisite_name 
        FROM PREREQUISITE
        JOIN COURSE ON PREREQUISITE.Prerequisite_number = COURSE.course_number
        WHERE PREREQUISITE.Course_number = %s
    """, (course_number,))
    prerequisites = cursor.fetchall()
    conn.close()
    return prerequisites
