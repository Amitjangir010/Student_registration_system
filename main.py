from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_mysqldb import MySQL
import pandas as pd
import csv
import pymysql
from io import StringIO

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Add your MySQL password here
app.config['MYSQL_DB'] = 'students'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# connecting with database
def connect_database(host, username, password):
    try:
        con = pymysql.connect(host=host, user=username, password=password)
        cursor = con.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS students')
        cursor.execute('USE students')
        cursor.execute('CREATE TABLE IF NOT EXISTS student(id INT NOT NULL PRIMARY KEY, name VARCHAR(30), mobile VARCHAR(10), email VARCHAR(30), address VARCHAR(100), gender VARCHAR(20), dob VARCHAR(20), date VARCHAR(50), time VARCHAR(50))')
        con.close()
        flash('Database connection is successful', 'success')
    except pymysql.Error as e:
        flash(f'Error: {str(e)}', 'error')

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        host = request.form['hostname']

        connect_database(host, username, password)

        if username == 'AMIT' and password == '1234':
            flash('Success', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Please enter correct credentials', 'error')

    return render_template('login.html')

# Dashboard Page
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # Handle delete student functionality here
        student_id = request.form['student_id']
        # Perform the deletion process

        # Redirect back to the dashboard

    elif request.method == 'GET':
        # Handle search functionality here
        search_query = request.args.get('search_query', '')
        if search_query:
            # Perform the search process based on the search_query
            with mysql.connection.cursor() as cursor:
                query = f"SELECT * FROM student WHERE name LIKE '%{search_query}%' OR mobile LIKE '%{search_query}%' OR email LIKE '%{search_query}%' OR address LIKE '%{search_query}%' OR gender LIKE '%{search_query}%' OR dob LIKE '%{search_query}%'"
                cursor.execute(query)
                students = cursor.fetchall()
        else:
            # Fetch all student data from the database
            with mysql.connection.cursor() as cursor:
                query = 'SELECT * FROM student'
                cursor.execute(query)
                students = cursor.fetchall()

        return render_template('dashboard.html', students=students, student={})  # Pass an empty student object

# Exporting the data as csv
@app.route('/export', methods=['POST'])
def export():
    # Fetch Student Data from Database
    with mysql.connection.cursor() as cursor:
        query = 'SELECT * FROM student'
        cursor.execute(query)
        students = cursor.fetchall()

    # Create a CSV string
    csv_data = StringIO()
    fieldnames = ['id', 'name', 'mobile', 'email', 'address', 'gender', 'dob']
    writer = csv.DictWriter(csv_data, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(dict(student))

    # Create a response with CSV content
    response = Response(csv_data.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=students.csv'

    return response

# adding new student
@app.route('/add_student', methods=['POST'])
def add_student():
    # Retrieve form data
    id = request.form['id']
    name = request.form['name']
    mobile = request.form['mobile']
    email = request.form['email']
    address = request.form['address']
    gender = request.form['gender']
    dob = request.form['dob']

    # Insert student record into the database
    with mysql.connection.cursor() as cursor:
        query = 'INSERT INTO student (id, name, mobile, email, address, gender, dob) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (id, name, mobile, email, address, gender, dob))
        mysql.connection.commit()

    flash('Student added successfully', 'success')
    return redirect(url_for('dashboard'))

# updating the row
@app.route('/update_student_form/<int:student_id>', methods=['GET'])
def update_student_form(student_id):
    # Retrieve student data based on the provided student ID
    with mysql.connection.cursor() as cursor:
        query = 'SELECT * FROM student WHERE id = %s'
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()

    # Render the template with the student data
    return render_template('update_student.html', student=student)

@app.route('/update_student', methods=['POST'])
def update_student():
    # Get the updated student data from the request form
    student_id = request.form['id']
    name = request.form['name']
    mobile = request.form['mobile']
    email = request.form['email']
    address = request.form['address']
    gender = request.form['gender']
    dob = request.form['dob']

    # Update the student data in the database
    with mysql.connection.cursor() as cursor:
        query = 'UPDATE student SET name = %s, mobile = %s, email = %s, address = %s, gender = %s, dob = %s WHERE id = %s'
        cursor.execute(query, (name, mobile, email, address, gender, dob, student_id))
        mysql.connection.commit()

    # Redirect to the dashboard or student list page
    return redirect('/dashboard')

# showing all student
@app.route('/show_student')
def show_student():
    # Retrieve student data from the database
    with mysql.connection.cursor() as cursor:
        query = 'SELECT * FROM student'
        cursor.execute(query)
        fetched_data = cursor.fetchall()

    # Render the template with the student data
    return render_template('dashboard.html', students=fetched_data)

# deleting student row
@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    # Delete student record from the database
    with mysql.connection.cursor() as cursor:
        query = 'DELETE FROM student WHERE id = %s'
        cursor.execute(query, (student_id,))
        mysql.connection.commit()

    flash('Student deleted successfully', 'success')
    return redirect(url_for('dashboard'))

# searching any row
@app.route('/search_student', methods=['POST'])
def search_student():
    # Retrieve form data
    search_query = request.form['search_query']

    # Search for student records in the database
    with mysql.connection.cursor() as cursor:
        query = 'SELECT * FROM student WHERE name LIKE %s OR email LIKE %s OR address LIKE %s OR gender LIKE %s'
        cursor.execute(query, (
        f'%{search_query}%', f'%{search_query}%', f'%{search_query}%',f'%{search_query}%'))
        students = cursor.fetchall()

    return render_template('dashboard.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
