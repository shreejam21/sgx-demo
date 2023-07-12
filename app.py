from flask import Flask, render_template, request, redirect, url_for
from sqlite import return_table
app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show-all')
def show_all_patients():
    return render_template("all.html", patients=return_table())

@app.route('/add', methods=['POST'])
def about():
    return render_template("all.html", patients=return_table())


if __name__ == '__main__':
    app.run(debug=True)
