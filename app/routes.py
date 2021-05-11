from flask import Flask, render_template, request, redirect, url_for
import random, copy

app = Flask(__name__)


#sets all the questions for test1
test1_data = {
    "When is it ok to text in your car?" : {
        "While driving" : False,
        "Engine off, parked in a safe place" : True,
        "At a red light" : False
    },
    "How close is considered tailgating?" : {
        "Less than 2s" : True,
        "Less than 3s" : False,
        "Less than 4s" : False

    },
    "How old should a child be before sitting infront of the front passenger airbag?" : {
            "At least 4" : False,
            "At least 6" : False,
            "At least 7" : True
    }
}
test1_original_questions = test1_data
test1_questions = copy.deepcopy(test1_original_questions)
test1_answers = []
def sampling(q, n=2):
    return random.sample(list(q.keys()), n)

def translate():
    return (lambda x: "True" if x else "False")
##test1 qeustions set


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


@app.route('/Test_1', methods=['GET', 'POST'])
def Test_1():
    test1_questions_shuffled = test1_questions
    return render_template('Test_1.html', q = test1_questions_shuffled, o = test1_questions)

@app.route('/quiz', methods=['POST'])
def quiz_answers():
    result = "<ol>"
    correct = 0
    for i in test1_questions.keys():
        if i in request.form:
            answered = request.form[i]
            if test1_original_questions[i][answered]:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test1_original_questions[i][answered]))
                print("question ", i, ": ", test1_original_questions[i][answered])
                test1_answers.append(test1_original_questions[i][answered])
                correct = correct+1
            else:
                result += "<li><u>{}</u></li>{} <b>{}</b>".format(i, answered, translate()(test1_original_questions[i][answered]))
                print("question ", i, ": ", test1_original_questions[i][answered])
                test1_answers.append(test1_original_questions[i][answered])
    for k in test1_answers: #puts all the answers into an array, this should get put into a database, guess we could cheese it by keeping it in python but that will get grotty
        print(k)
    result += "</ol>"
    result += '<h1>Answers Correct: <u>'+str(correct)+'</u></h1>'
    return result
    

if __name__=='__main__':
    app.run(debug=True)