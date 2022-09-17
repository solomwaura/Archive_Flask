import email
from flask import request
from flask import Blueprint
from flask import render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])  
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/register',methods=['GET','POST'])
def register():
    if request.method =="POST":
        firstName = request.form.get('fname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if firstName == "":
            flash('Please enter your first name',category='error')
        elif len(email) < 4:
            flash('Email must be longer than 3 characters',category='error')
        elif len(password1) < 8:
            flash('Password length must be longer than 7 characters',category='error')
        elif password2 == "":
            flash('Please confirm your password',category='error')
        elif password1 != password2 :
            flash('The two passwords do not match',category='error')
        else:
            #add user to the db
            flash('Account created succcessfully',category='success')
    
    return render_template('signup.html')