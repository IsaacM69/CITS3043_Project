from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required 
from app.models import User, Scores
from flask import request
from werkzeug.urls import url_parse
from app.forms import LoginForm

class accountControllers():

    def login():
        form = LoginForm()
        if form.validate_on_submit(): #will return false for a get request
            User = User.query.filter_by(id=form.student_number.data).first()
            if User is None or not User.check_password(form.pin.data):
                flash('invalid username or data')
                return redirect(url_for('login'))
                login_user(student, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc !='':
                next_page = 'index'
                return redirect(url_for(next_page))
        return render_template('login.html',title="Sign in", form = form)


def CreateAccount():
    form= CreateAccount()#??include current user data by default
    if form.validate_on_submit(): #will return false for a GET request
      User = User.query.filter_by(id=form.email.data).first()
      if User is None:
        flash('Unrecognized email')
        return redirect(url_for('index'))
      if current_user.is_authenticated:
        if not User.check_password(form.password.data):
          flash('Incorrect Password')
          return redirect(url_for('index'))
      elif User.password_hash is not None:
        flash('Email already has account')
        return redirect(url_for('index'))
      User.Password(form.Password.data)
      User.First_name = form.First_name.data
      User.Last_name = form.Last_name.data
  ##    db.session.commit()
      login_user(User, remember=False)
      return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
  