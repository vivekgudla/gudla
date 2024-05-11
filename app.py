from flask import Flask, render_template, request, redirect, url_for

import sqlite3

app = Flask(__name__)

def create_connection():
    conn = sqlite3.connect('user2.db')
    return conn

def create_table():
    conn = create_connection()
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS student(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        fathername TEXT NOT NULL,
        mothername TEXT NOT NULL,
        gender TEXT NOT NULL,
        cnum TEXT NOT NULL,
        date INTEGER NOT NULL,
        marks INTEGER NOT NULL,
        INTERMEDIATE marks INTEGER NOT NULL,
        DEGREE marks INTEGER NOT NULL,
        address TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        fathername = request.form['fathername']
        mothername = request.form['mothername']
        gender = request.form['gender']
        cnum = request.form['number']
        date = request.form['date']
        marks = request.form['marks']
        intermediate = request.form['INTERMEDIATE ']
        degree = request.form['DEGREE ']
        address = request.form['add']
        email = request.form['mail']
        password = request.form['pass']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO student(fname, lname, fathername, mothername, gender, cnum, date, marks, INTERMEDIATE, DEGREE, address, email, password) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (fname, lname, fathername, mothername, gender, cnum, date, marks,INTERMEDIATE, DEGREE, address, email, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['mail']
        password = request.form['pass']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM student WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect(url_for('user_details', user_id=user[0]))
        else:
            return "Login failed. Please check your email and password."
    return render_template("login.html")

@app.route('/user_details/<int:user_id>')
def user_details(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student WHERE ID = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return render_template('user_details.html', user=user)
    else:
        return "User not found."


if __name__ == '__main__':
    create_table()
    app.run(debug=True)