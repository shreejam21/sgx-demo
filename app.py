from flask import Flask, render_template, request, redirect, url_for
from sqlite import return_table, get_patient
app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show-all')
def show_all_patients():
    return render_template("all.html", patients=return_table())

@app.route('/get-patient-prompt')
def get_patient_prompt():
    return render_template("get_patient_prompt.html")

@app.route('/get-patient-result', methods=['GET', 'POST'])
def get_patient_result():
    if request.method == 'POST':
      name = request.form['Name']
      age = request.form['Age']
      gender = request.form['Gender']
      return render_template("all.html", patients=get_patient(name, age, gender))

if __name__ == '__main__':
    app.run(debug=True)
