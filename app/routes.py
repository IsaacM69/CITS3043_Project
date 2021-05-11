from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from flask_login import current_user,login_user, logout_user, login_required
from werkzeug.urls import url_parse

app = Flask(__name__)

@app.route('/home')
def home():
    return "Sup pussys" 

@app.route('/')
def Homepage():
    return render_template('Homepage.html')

@app.route('/CreateAccount', methods=['GET', 'POST'])
def CreateAccount():

    error = None
    if request.method =='POST':

        if request.form['password'] != request.form['Cpass']:
            error = "Password don't match!"
            return render_template('CreateAccount.html', error = error)

        elif request.form['fname'] == "" or request.form['lname'] == "" or request.form['email'] == "" or request.form['Cpass'] == "" or request.form['password'] == "":
            error = "Complete all fields!"
            return render_template('CreateAccount.html', error = error)

        else:

            return redirect(url_for('Homepage'))

    return render_template('CreateAccount.html')

@app.route('/Login', methods=['GET', 'POST'])
def login():
    
    error = None
    if request.method =='POST':

        if request.form['pass'] != 'bofa' or request.form['email'] != 'garth':
            error = "Incorrect password or email"

        else:

            return redirect(url_for('Homepage'))
    return render_template('Login.html', error = error)


@app.route('/Module_1')
def Module_1():
    return render_template('Module_1.html')

@app.route('/Module_2')
def Module_2():
    return render_template('Module_2.html')

@app.route('/Module_3')
def Module_3():
    return render_template('Module_3.html')

@app.route('/Test_1', methods=['GET', 'POST'])
def Test_1():
    error = None
    if request.method == 'POST':
        question1 = request.form['q1']
        print("q1: ", question1)

        question2 = request.form['q2']
        print("q2: ", question2)

    
    return render_template('Test_1.html')

if __name__=='__main__':
    app.run(debug=True)