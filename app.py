from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)




@app.route('/')
def hello_world():
    return "<h1> HELLO WORLD !!</h1>"

@app.route('/add', methods=['POST'])
def about():
    return "<h1> HELLO ABOUT !!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
