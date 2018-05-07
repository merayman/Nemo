import os as os
from flask import Flask, render_template, render_template_string
import pymysql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('welcome.html')


if __name__ == '__main__':
    #app.debug = True: debug mode
    host = os.environ.get('IP')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)