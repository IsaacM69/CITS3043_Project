from flask import Flask, render_template, request, redirect, url_for
from flask_login import current_user,login_user, logout_user, login_required, UserMixin
from werkzeug.urls import url_parse
import random, copy
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
import sqlalchemy
from wtforms.validators import InputRequired, Length, regexp, EqualTo
from wtforms import  StringField, PasswordField, SubmitField, SelectField
from config import Config
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
##from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config.from_object(Config)
db = SQLAlchemy(app)
##migrate = Migrate(app, db)

class CreateAccount(FlaskForm):
  First_name = StringField('First Name', validators=[InputRequired(), Length(max=64)])
  Last_name = StringField('Last Name', validators=[InputRequired(), Length(max=64)])
  Email = StringField('Email', validators=[InputRequired(), Length(max=64)])
  Password = PasswordField('Password',  validators=[InputRequired(), Length(max=64)])
  Confirm_Password = PasswordField('Confirm Password', validators=[EqualTo('Password'), Length(max=64)])

class LoginForm(FlaskForm):
  Email = StringField('Email')
  Password = PasswordField('Password')

#sets all the questions for test1
test1_data = {
    "When is it ok to text in your car?" : {
        "While driving" : "Incorrect",
        "Engine off, parked in a safe place" : "Correct",
        "At a red light" : "Incorrect"
    },
    "How close is considered tailgating?" : {
        "Less than 2s" : "Correct",
        "Less than 3s" : "Incorrect",
        "Less than 4s" : "Incorrect"

    },
    "How old should a child be before sitting infront of the front passenger airbag?" : {
            "At least 4" : "Incorrect",
            "At least 6" : "Incorrect",
            "At least 7" : "Correct"
    }
}
test1_original_questions = test1_data
test1_questions = copy.deepcopy(test1_original_questions)
test1_answers = []
c1 = 0
#sets all the questions for test2
test2_data = {
    "What should you do immediately after a crash?" : {
        "Stop in a safe place, turn on your hazard lights" : "Correct",
        "Exit vehicle and divert traffic" : "Incorrect",
        "Drive off" : "Incorrect"
    },
    "What details of the other driver do you not need?" : {
        "Name" : "Inorrect",
        "License number" : "Incorrect",
        "Facebook aacount" : "Correct"

    },
    "Are you obligated to take the first tow truck that arrives on the scene?" : {
            "Yes" : "Incorrect",
            "No" : "Correct",
    }
}
test2_original_questions = test2_data
test2_questions = copy.deepcopy(test2_original_questions)
test2_answers = []
c2 = 0

#sets all the questions for test3
test3_data = {
    "What isn't a potential conequence of speeding?" : {
        "Harming yourself and others" : "Inorrect",
        "Speeding fines" : "Incorrect",
        "Demerit points" : "Incorrect",
        "Saving lives" : "Correct",
        "Annoying the nighbours" : "Incorrect"

    },
    "What percent of accidents involved distracted drivers in 2016?" : {
        "13%" : "Inorrect",
        "16%" : "Correct",
        "19%" : "Inorrect",
        "21%" : "Inorrect"

    },
    "When should you report a car accident to the police?" : {
            "Occured on any public road" : "Incorrect",
            "If it resulted in bodily harm" : "Inorrect",
            "Occured in a carpark" : "Incorrect",
            "All of the above" : "Correct"
            
    },
    "Who can you not deny tow trucks from?" : {
        "Insurance" : "Inorrect",
        "Police" : "Correct",
        "Roadside" : "Inorrect"

    },
    "Who should you call if someone is injured in the crash?" : {
        "Ambulance" : "Correct",
        "Insurance" : "Incorrect",
        "Dad" : "Incorrect"

    },
}
test3_original_questions = test3_data
test3_questions = copy.deepcopy(test3_original_questions)
test3_answers = []
c3 = 0

##prety usless defineitions vv
def sampling(q, n=2):
    return random.sample(list(q.keys()), n)

def translate():
    return (lambda x: "True" if x else "False")


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('Homepage.html', a1 = test1_answers, a2 = test2_answers, a3 = test3_answers, c1 = c1, c2 = c2, c3 = c3)

@app.route('/', methods=['GET', 'POST'])
def Homepage():
    return render_template('Homepage.html', a1 = test1_answers, a2 = test2_answers, a3 = test3_answers, c1 = c1, c2 = c2, c3 = c3)

@app.route('/CreateAccount', methods=['GET', 'POST'])
def CreateAccount():
    form = CreateAccount()

    if request.method =='POST':
        newUser = User(id = random.randrange(0, 100000), firstName = form.First_name.data, lastName = form.Last_name.data, email = form.email.data, password_hash = form.email.password)
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser)
        return render_template('Homepage.html')

    return render_template('CreateAccount.html')

@app.route('/Login', methods=['GET', 'POST'])
def login():
    
    error = None
    if request.method =='POST':
        user =  User.query.filter_by(id=request.form['email']).first()
        if user:
            if request.form['pass'] != user.password_hash:
                error = "Incorrect password or email"

        else:

            return redirect(url_for('Homepage'))
    return render_template('Login.html', error = error)


@app.route('/Module_1')
def Module_1():
    if not current_user.is_authenticated:
        return redirect(url_for('Login'))
    return render_template('Module_1.html')

@app.route('/Module_2')
def Module_2():
    return render_template('Module_2.html')

@app.route('/Module_3')
def Module_3():
    return render_template('Module_3.html')

@app.route('/Test_1', methods=['GET', 'POST'])
def Test_1():
    test1_questions_shuffled = test1_questions
    return render_template('Test_1.html', q = test1_questions_shuffled, o = test1_questions)

@app.route('/Test_1_Results', methods=['POST'])
def quiz_answers():
    test1_answers = []
    result = "<ol>"
    correct = 0
    for i in test1_questions.keys():
        if i in request.form:
            answered = request.form[i]
            if test1_original_questions[i][answered]:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test1_original_questions[i][answered]))
                print("question ", i, ": ", test1_original_questions[i][answered])
                test1_answers.append([i, test1_original_questions[i][answered]])
                if test1_original_questions[i][answered] == "Correct":
                    correct +=1
            else:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test1_original_questions[i][answered]))
                print("question ", i, ": ", test1_original_questions[i][answered])
                test1_answers.append([i, test1_original_questions[i][answered]])
    for k in test1_answers: #puts all the answers into an array, this should get put into a database, guess we could cheese it by keeping it in python but that will get grotty
        print(k)
    print(len(test1_answers))
    c1 = correct
    result += "</ol>"
    result += '<h1>Answers Correct: <u>'+str(correct)+'</u></h1>'
    return render_template('Test_1_results.html', c = correct, a = test1_answers)
    

@app.route('/Test_2', methods=['GET', 'POST'])
def Test_2():
    test2_questions_shuffled = test2_questions
    return render_template('Test_2.html', q = test2_questions_shuffled, o = test2_questions)

@app.route('/Test_2_Results', methods=['POST'])
def quiz2_answers():
    test2_answers = []
    result = "<ol>"
    correct = 0
    for i in test2_questions.keys():
        if i in request.form:
            answered = request.form[i]
            if test2_original_questions[i][answered]:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test2_original_questions[i][answered]))
                print("question ", i, ": ", test2_original_questions[i][answered])
                test2_answers.append([i, test2_original_questions[i][answered]])
                if test2_original_questions[i][answered] == "Correct":
                    correct +=1
            else:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test2_original_questions[i][answered]))
                print("question ", i, ": ", test2_original_questions[i][answered])
                test2_answers.append([i, test2_original_questions[i][answered]])
    for k in test2_answers: #puts all the answers into an array, this should get put into a database, guess we could cheese it by keeping it in python but that will get grotty
        print(k)
    print(len(test2_answers))
    c2 = correct
    result += "</ol>"
    result += '<h1>Answers Correct: <u>'+str(correct)+'</u></h1>'
    return render_template('Test_2_results.html', c = correct, a = test2_answers)
    


@app.route('/Test_3', methods=['GET', 'POST'])
def Test_3():
    test3_questions_shuffled = test3_questions
    return render_template('Test_3.html', q = test3_questions_shuffled, o = test3_questions)

@app.route('/Test_3_Results', methods=['POST'])
def quiz3_answers():
    test3_answers = []
    result = "<ol>"
    correct = 0
    for i in test3_questions.keys():
        if i in request.form:
            answered = request.form[i]
            if test3_original_questions[i][answered]:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test3_original_questions[i][answered]))
                print("question ", i, ": ", test3_original_questions[i][answered])
                test3_answers.append([i, test3_original_questions[i][answered]])
                if test3_original_questions[i][answered] == "Correct":
                    correct +=1
            else:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test3_original_questions[i][answered]))
                print("question ", i, ": ", test3_original_questions[i][answered])
                test3_answers.append([i, test3_original_questions[i][answered]])
    for k in test3_answers: #puts all the answers into an array, this should get put into a database, guess we could cheese it by keeping it in python but that will get grotty
        print(k)
    print(len(test3_answers))
    c3 = correct
    result += "</ol>"
    result += '<h1>Answers Correct: <u>'+str(correct)+'</u></h1>'
    return render_template('Test_3_results.html', c = correct, a = test3_answers)
    





class User(UserMixin,db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)

    firstName = db.Column(db.String(64), index=True, unique=False)
    lastName = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    Scores = db.relationship('score', backref = 'user',  lazy = 'dynamic')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.firstName)

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.firstName

class Scores(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)

    score_ID = db.Column(db.Integer, db.ForeignKey('user.id')) 
    Mod_1 = db.Column(db.Integer, index=True, unique=False)
    Mod_2 = db.Column(db.Integer, index=True, unique=False)
    Mod_3 = db.Column(db.Integer, index=True, unique=False)
    finalScore = db.Column(db.Integer, index=True, unique=False)
    totalScore = db.Column(db.Integer, index=True, unique=False)



if __name__=='__main__':
    app.run(debug=True)