from flask import Flask, render_template, request, redirect, url_for
from sqlite import return_table
import sqlite

app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show-all')
def show_all_patients():
    return render_template("all.html", patients=return_table())


@app.route('/add-patient', methods= ['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        condition = request.form['condition']

        sqlite.add_patient(name,age,gender,condition)

        return "Patient Added Succesfully"
        
    return render_template('add-patient.html')

    


if __name__ == '__main__':
    app.run(debug=True)
