from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital"
)
cursor = db.cursor()

# Route to render the form
@app.route('/')
def login():
    return render_template('login.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        regno = request.form['regno']
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        dob = request.form['dob']
        dept = request.form['dept']
        phn_no = request.form['phn_no']
        
        
        # Insert data into MySQL database
        cursor.execute("INSERT INTO OutPatient (REGNO,NAME,GENDER,AGE,DOB,DEPARTMENT,PHONE_NO) VALUES (%s, %s)", (regno,name,gender,age,dob,dept,phn_no))
        db.commit()
        
        return redirect(url_for('login'))  # Redirect to the form page

if __name__ == '__main__':
    app.run(debug=True)
