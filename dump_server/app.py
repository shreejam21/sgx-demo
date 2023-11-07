from flask import Flask, render_template, request, redirect, url_for

import docker_dump

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        secret = request.form['secret']
        container_name = request.form['containerName']

        file_contents, grep_output = docker_dump.dump_data(secret, container_name)

        return file_contents, 200
    
    return render_template("dump-memory.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5005, ssl_context='adhoc', debug=True)
