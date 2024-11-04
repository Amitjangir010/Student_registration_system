from flask import Flask, render_template, request, redirect, url_for, Response, flash

app = Flask(__name__)
app.secret_key = 'random_key_for_sessions'

students = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login logic here
        hostname = request.form['hostname']
        username = request.form['username']
        password = request.form['password']
        # This is a placeholder logic; replace it with actual logic if needed
        if hostname=="root" and username=="abcd" and password=="1234":
            flash("Connected successfully!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Connection failed!", "error")
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', students=students)


@app.route('/add_student', methods=['POST'])
def add_student():
    student = {
        'id': request.form['id'],
        'name': request.form['name'],
        'mobile': request.form['mobile'],
        'email': request.form['email'],
        'address': request.form['address'],
        'gender': request.form['gender'],
        'dob': request.form['dob']
    }
    students.append(student)
    return redirect(url_for('dashboard'))


@app.route('/search_student', methods=['POST'])
def search_student():
    search_query = request.form['search_query'].lower()
    filtered_students = [
        student for student in students
        if search_query in student['id'].lower() or search_query in
        student['name'].lower() or search_query in student['mobile'].lower()
        or search_query in student['email'].lower()
        or search_query in student['address'].lower() or search_query in
        student['gender'].lower() or search_query in student['dob'].lower()
    ]
    return render_template('dashboard.html', students=filtered_students)


@app.route('/export', methods=['POST'])
def export():
    csv_data = "ID,Name,Mobile,Email,Address,Gender,DOB\n"
    for student in students:
        csv_data += f"{student['id']},{student['name']},{student['mobile']},{student['email']},{student['address']},{student['gender']},{student['dob']}\n"

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=students.csv"})


@app.route('/show_student', methods=['GET'])
def show_student():
    return render_template('dashboard.html', students=students)


@app.route('/delete_student/<student_id>', methods=['POST'])
def delete_student(student_id):
    global students
    students = [student for student in students if student['id'] != student_id]
    return redirect(url_for('dashboard'))


@app.route('/update_student_form/<student_id>', methods=['GET'])
def update_student_form(student_id):
    student = next(student for student in students
                   if student['id'] == student_id)
    return render_template('update_student.html', student=student)


@app.route('/update_student/<student_id>', methods=['POST'])
def update_student(student_id):
    for student in students:
        if student['id'] == student_id:
            student['name'] = request.form['name']
            student['mobile'] = request.form['mobile']
            student['email'] = request.form['email']
            student['address'] = request.form['address']
            student['gender'] = request.form['gender']
            student['dob'] = request.form['dob']
            break
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
