import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from website.web_config import db
from website.models import Category, Complaints, Student
from werkzeug.utils import secure_filename
app = Flask(__name__)

def send_complaint():
    user_id = session.get('student_id')
    student = Student.query.get(user_id)
    category = Category.query.all()
    
    if request.method == 'POST':
        category = request.form['category']
        complaintDetails = request.form['complaintDetails']

        if not category or not complaintDetails:
            flash('Please fill out field category or complaintDetails', category='error')
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
            flash('Complaint submitted successfully!', category='success')
            print('Complaint submitted successfully!')
            return redirect(url_for('com_send_message'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error submitting complaint: {e}', category='error')
            print(f'Error submitting complaint: {e}')
            return redirect(url_for('com_send_message'))

    return render_template('compliant_form.html', user=student, category=category)


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
        
        print(name)
        print(email)
        print(year)
        print(major)
        if len(phone) < 5:
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
            db.session.commit()
            print("update successfully")
            return redirect(url_for('clientProfile'))
        
        return render_template('clientprofile.html', user=student)