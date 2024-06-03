import os
import re
from flask import Flask, flash, redirect, render_template, request, session, url_for
from website.web_config import db
from website.models import Category, Complaints, Student
from werkzeug.utils import secure_filename
app = Flask(__name__)

def send_complaint():
    user_id = session.get('student_id')
    category = Category.query.all()
    student = Student.query.get(user_id)
    if student:
        if request.method == 'POST':
            category = request.form['category']
            complaintDetails = request.form['complaintDetails']

            if not category or not complaintDetails:
                flash('Please fill out field category or complaintDetails', 'complaintsformerror')
                print("please fill out this field")
                return redirect(url_for('com_send_message'))

            new_complaint = Complaints(
                complaint_letter=complaintDetails,
                status = "Unsolved",
                student_id=user_id,
                category_id=category,
            )
            try:
                db.session.add(new_complaint)
                db.session.commit()
                flash('Complaint submitted successfully!', 'complaintsformsuccess')
                return redirect(url_for('com_send_message'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error submitting complaint: {e}', 'complaintsformerror')
                return redirect(url_for('com_send_message'))

        return render_template('compliant_form.html', user=student, category=category)
    
    session.pop('student_id', None)
    return render_template('homepage.html')


# image upload
UPLOAD_FOLDER = 'Website/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  
# update client profile image 
def clientprofile():
    user_id = session.get('student_id')
    student = Student.query.get(user_id)
    if student:
        if request.method == 'POST':
            if 'profileImage' not in request.files:
                print('No file part')
                return redirect(request.url)
            
            file = request.files['profileImage']
            
            if file:
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    if filename:
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        student.student_image = filename
                        db.session.commit()
                        print("successfully uploaded")
                        return redirect(url_for('clientProfile'))
                else:
                    flash('Not allowed file type', 'clientInfoerror')
            else:
                flash('please fill file','clientInfoerror')

        return render_template('clientprofile.html', user=student)
    
    # student is not present in database
    session.pop('student_id', None)
    return render_template('homepage.html')

def emailPattern(email):
    e_pattern = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    return re.match(e_pattern, email) is not None

# update client information
def updateclientinformation():
    user_id = session.get('student_id')
    student = Student.query.get(user_id)
    
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get('email')
        year = request.form.get("year")
        major = request.form.get("major")
        phone = request.form.get("phone")
        
        if not name:
            flash('Please fill name', 'clientInfoerror')
            return redirect(url_for('clientProfile'))
        if not email:
            flash('Please fill email', 'clientInfoerror')
            return redirect(url_for('clientProfile'))
        if not emailPattern(email):
            flash('Invaild email', 'clientInfoerror')
            return redirect(url_for('clientProfile'))
        if not year:
            flash('Please fill Batch', 'clientInfoerror')
            return redirect(url_for('clientProfile'))
        if not major:
            flash('Please fill major', 'clientInfoerror')
            return redirect(url_for('clientProfile'))
        if not phone:
            flash('Please fill phone number', 'clientInfoerror')
            
        
        student.student_name = name
        student.student_email = email
        student.student_year = year
        student.student_major = major
        student.student_phone = phone
        db.session.commit()

        return redirect(url_for('clientProfile'))