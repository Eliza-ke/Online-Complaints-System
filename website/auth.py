import re
from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import Admin, ForgotPassword, Student
from website.web_config import db

def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email:
            flash('Please fill email', 'authfillerror')
            return redirect(url_for('SignIn'))
        if not password:
            flash('Please fill password', 'authfillerror')
            return redirect(url_for('SignIn'))
        
        student = Student.query.filter_by(student_email=email).first()
        admin = Admin.query.filter_by(admin_email=email).first()

        if student:
            if check_password_hash(student.student_password, password):
                session['student_id'] = student.id
                return redirect(url_for('home'))
            else:
                flash('Incorrect password', 'autherror')
                return redirect(url_for('SignIn'))
        elif admin:
            if check_password_hash(admin.admin_password, password):
                myadmin = {
                            "admin_id": admin.id,
                            "admin_name": admin.admin_name,
                            "admin_email": admin.admin_email,
                            "admin_profile": admin.admin_image,
                        }
                session['admin_id'] = admin.id
                session['admin'] = myadmin
                return redirect(url_for('viewCategory'))
            else:
                flash('Incorrect password', 'autherror')
                return redirect(url_for('SignIn'))
        else:    
            flash('Email does not exist.', 'autherror')
    return render_template("signinform.html")

def strongPassword(password):
    pw_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    return re.match(pw_pattern, password ) is not None

def emailPattern(email):
    e_pattern = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    return re.match(e_pattern, email) is not None
    
def signup():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get('email')
        year = request.form.get("year")
        major = request.form.get("major")
        phone = request.form.get("phone")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        student_info = Student.query.filter_by(student_email=email).first()
        if student_info:
            flash('email is already exist', 'autherror')
        elif not email:
            flash('Please fill your Email', 'autherror')
            return redirect(url_for('Signup'))
        elif not name:
            flash('Please fill your Name', 'autherror')
            return redirect(url_for('Signup'))
        elif not year:
            flash('Please select a year', 'autherror')
            return redirect(url_for('Signup'))
        elif not major:
            flash('Please select a major', 'autherror')
            return redirect(url_for('Signup'))
        elif not phone or len(phone) < 7:
            flash('Please fill your real phone number', 'autherror')
            return redirect(url_for('Signup'))
        elif not password1:
            flash('Please fill password', 'autherror')
        elif not password2:
            flash('Please fill confirm password', 'autherror')
        elif not emailPattern(email):
            flash('Invaild email', 'autherror')
            return redirect(url_for('Signup'))
        elif password1 != password2:
            flash('Password does not match', 'autherror')
            return redirect(url_for('Signup'))
        elif not strongPassword(password1) and len(password1) < 8:
            flash('Password must be included Uppercase, Lowercase, Number and Special Characters. Password length must be greater than 8 characters', 'autherror')
            return redirect(url_for('Signup'))
        else:
            profileImg = "defaultprofile.png"
            new_student = Student(
                student_email=email,
                student_name=name,
                student_password=generate_password_hash(password1, method='pbkdf2:sha256'),
                student_year=year,
                student_major=major,
                student_phone=phone,
                student_image=profileImg
            )
            db.session.add(new_student)
            db.session.commit()
            flash("Account created successfully!", 'authsuccess')
            return redirect(url_for('SignIn'))
        
    return render_template("signupform.html")
            

def forgotpassword():

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        reason = request.form.get('reason')
        
        if not name:
            flash('Please fill name', 'forgotpassworderror')
            return redirect(url_for('forgotPassword'))
        
        if not email:
            flash('Please fill email', 'forgotpassworderror')
            return redirect(url_for('forgotPassword'))
        
        if not reason:
            flash('Please fill reason for reset password', 'forgotpassworderror')
            return redirect(url_for('forgotPassword'))
        
        student = Student.query.filter_by(student_email=email, student_name=name).first()

        if student:
            student_id = student.id
            new_forgotpassword = ForgotPassword(student_id=student_id, reason=reason)
            db.session.add(new_forgotpassword)
            db.session.commit()
            print("successfully submitted!!!")
            return redirect(url_for('home'))
        else:    
            flash('Your account does not exist.', category='forgotpassworderror')
    return render_template("forgotPassword.html")


# def admin_create():
#     profileImg = "defaultprofile.png"
#     new_admin = Admin(
#         admin_name="eliza",
#         admin_email="eliza@gmail.com",
#         admin_phone="0932658471",
#         admin_password=generate_password_hash("abc123", method='pbkdf2:sha256'),
#         admin_image=profileImg
#     )
#     db.session.add(new_admin)
#     db.session.commit()            
            
            
            