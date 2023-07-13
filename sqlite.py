import sqlite3

DATABASE = 'patients.db'

#Function to Create Table if table doesnt exist
def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 gender TEXT NOT NULL,
                 condition TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#Function to Return Table 
def return_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM patients")
    patients = c.fetchall()
    conn.close()
    return patients
    # return render_template('index.html', patients=patients)

#Function to Add patients to the Table / DB
def add_patient(name, age, gender, condition):
    
    # if request.method == 'POST':
    #     name = request.form['name']
    #     age = request.form['age']
    #     gender = request.form['gender']
    #     condition = request.form['condition']
        # return redirect(url_for('index')) 

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO patients (name, age, gender, condition) VALUES (?, ?, ?, ?)",
                (name, age, gender, condition))
    conn.commit()
    conn.close()
        

    # return render_template('add.html')

#function to query Data
def get_patient(name):
    
    # if request.method == 'POST':
    #     name = request.form['name']
    #     age = request.form['age']
    #     gender = request.form['gender']
    #     condition = request.form['condition']
        # return redirect(url_for('index')) 

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM patients WHERE name = ?", (name,))
    data = c.fetchall()
    conn.close()
    return data

# create_table()
# print(get_patient("Shreejan", '', ''))
# add_patient("Shreejan", '22', 'M', 'Doesnt not FLASK')
# add_patient("Aayush", '21', 'M', 'Knows FLASK')
# add_patient("Phil King", '', 'M', 'Knows SGX')
# get_patient("Shreejan")
# get_patient("Josh")
