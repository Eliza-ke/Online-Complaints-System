from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import Admin, Student
from website.web_config import db

def signin():
    # admin_create()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Please fill email or password fields', category='error')
            return redirect(url_for('SignIn'))
        
        student = Student.query.filter_by(student_email=email).first()
        admin = Admin.query.filter_by(admin_email=email).first()

        if student:
            if check_password_hash(student.student_password, password):
                flash("sign in successfully!", category='success')
                session['student_id'] = student.id
                return redirect(url_for('home'))
            else:
                flash('Incorrect password', category='error')
                return redirect(url_for('SignIn'))
        elif admin:
            if check_password_hash(admin.admin_password, password):
                flash("sign in successfully!", category='success')
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
                flash('Incorrect password', category='error')
                return redirect(url_for('SignIn'))
        else:    
            flash('Email does not exist.', category='error')
    return render_template("signinform.html")

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
            flash('email is already exist', category='error')
        elif len(email) < 5:
            flash('Invaild email', category='error')
            return redirect(url_for('Signup'))
        elif len(name) < 2:
            flash('Name must be longer than 2 letters', category='error')
            return redirect(url_for('Signup'))
        elif len(year) < 2:
            flash('Batch must be longer than 2 letter', category='error')
            return redirect(url_for('Signup'))
        elif len(major) < 2:
            flash('Major must be longer than 2 letter', category='error')
            return redirect(url_for('Signup'))
        elif len(phone) < 5:
            flash('Phone Number must be longer than 5 letters', category='error')
            return redirect(url_for('Signup'))
        elif len(password1) < 7:
            flash('Password must be greater than 7', category='error')
            return redirect(url_for('Signup'))
        elif password1 != password2:
            flash('Password does not match', category='error')
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
            flash("Account created successfully!", category='success')
            return redirect(url_for('SignIn'))
        
    return render_template("signupform.html")
            
    
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
            