from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import random

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(host="localhost",user="root",password="root",database='Hospital')
cursor = db.cursor()
cursor.execute('Create table if not exists Registration(REGNO int(5) primary key,NAME varchar(20)) ')
cursor.execute('Create table if not exists OutPatient(REGNO int(5) foreign key references Registration(REGNO),NAME varchar(20),GENDER varchar(10),AGE int(3),DOB date,DEPARTMENT varchar(15),PHN_NO int(10))')

# Route to render the form
@app.route('/login')
def login():
    return render_template('login.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        regno = request.form['reg_no']
        name = request.form['fname']
        gender = request.form['gender']
        age = request.form['age']
        dob = request.form['dob']
        dept = request.form['department']
        phn_no = request.form['phoneno']
        
        if regno=='':
            r=random.randint(1000,99999)
            
            
        # Insert data into MySQL database
        cursor.execute("INSERT INTO OutPatient(REGNO,NAME,GENDER,AGE,DOB,DEPARTMENT,PHN_NO) VALUES(%s,%s,%s,%s,%s,%s,%s)", (regno,name,gender,age,dob,dept,phn_no))
        db.commit()
        
        return redirect(url_for('login'))  # Redirect to the form page

if __name__ == '__main__':
    app.run(debug=True)
