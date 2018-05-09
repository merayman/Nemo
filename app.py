import os as os
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('welcome.html')


@app.route('/home', methods=["POST", "GET"])
def loginSignin():
    username = request.form["loginEmail"]
    password = request.form["loginPassword"]
    print(username)
    return render_template('welcome.html')




if __name__ == '__main__':
    app.run()