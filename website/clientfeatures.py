import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from website.web_config import db
from website.models import Complaintone, Student
from werkzeug.utils import secure_filename
app = Flask(__name__)

def send_complaint():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_id = request.form['user_id']
        user_email = request.form['user_email']
        user_phone = request.form['user_phone']
        user_selector = request.form['user_selector']
        user_mail_one = request.form['user_mail_one']


        if not user_name or not user_id or not user_email or not user_phone or not user_selector or not user_mail_one:
            flash('Please fill out all fields')
            return redirect(url_for('com_send_message'))

        new_complaint = Complaintone(
            user_name=user_name,
            user_id=user_id,
            user_email=user_email,
            user_phone=user_phone,
            user_selector=user_selector,
            user_mail_one=user_mail_one
        )
        try:
            db.session.add(new_complaint)
            db.session.commit()
            flash('Complaint submitted successfully!')
            return redirect(url_for('com_send_message'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error submitting complaint: {e}')
            return redirect(url_for('com_send_message'))

    return render_template('compliant_form.html')

UPLOAD_FOLDER = 'Website/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  
def clientprofile():
    user_id = session.get('student_id')
    student = Student.query.get(user_id)
    if request.method == 'POST':
        if 'profileImage' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['profileImage']
        
        if file:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                student.student_image = filename
                db.session.commit()
                print("successfully uploaded")
                return redirect(url_for('clientProfile'))

    return render_template('clientprofile.html', user=student)
  
def updateclientinformation():
    user_id = session.get('student_id')
    student = Student.query.get(user_id)
    
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get('email')
        year = request.form.get("year")
        major = request.form.get("major")
        phone = request.form.get("phone")
        
        if len(email) < 5:
            flash('Invaild email', category='error')
        elif len(name) < 2:
            flash('Name must be longer than 2 letters', category='error')
        elif len(year) < 2:
            flash('Batch must be longer than 2 letter', category='error')
        elif len(major) < 2:
            flash('Major must be longer than 2 letter', category='error')
        elif len(phone) < 5:
            flash('Phone Number must be longer than 5 letters', category='error')
        else:
            student.student_name = name
            student.student_email = email
            student.student_year = year
            student.student_major = major
            student.student_phone = phone
            print("update successfully")
            return redirect(url_for('clientProfile'))
        
        return render_template('clientprofile.html', user=student)