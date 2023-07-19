from flask import Flask, render_template, request, redirect, url_for

import sqlite

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show-all')
def show_all_patients():
    return render_template("all.html", patients=sqlite.return_table())

@app.route('/get-patient-prompt')
def get_patient_prompt():
    return render_template("get_patient_prompt.html")

@app.route('/get-patient-result', methods=['GET', 'POST'])
def get_patient_result():
    if request.method == 'POST':
      name = request.form['Name']
      return render_template("all.html", patients=sqlite.get_patient(name))

@app.route('/add-patient', methods= ['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        condition = request.form['condition']

        sqlite.add_patient(name,age,gender,condition)

        return render_template('patient-added.html')
        
    return render_template('add-patient.html')

  

if __name__ == '__main__':
    sqlite.create_table()
    app.run(host = '0.0.0.0', port = 5000, ssl_context='adhoc', debug=True)
