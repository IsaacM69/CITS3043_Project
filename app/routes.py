from flask import Flask, render_template, request, redirect, url_for

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

        else:

            return redirect(url_for('Homepage'))
    return render_template('CreateAccount.html', error = error)

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


@app.route('/Test_1')
def Test_1():
    return render_template('Test_1.html')

if __name__=='__main__':
    app.run(debug=True)