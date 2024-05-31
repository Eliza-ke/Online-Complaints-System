import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from website.models import Admin, Category, Complaints, Student
from website.web_config import db
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'Website/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    if '.' in filename:
        extension = filename.rsplit('.', 1)[1].lower()
        if extension in ALLOWED_EXTENSIONS:
            return True
    return False
           
def viewcategory():
    categories = Category.query.all()
    return render_template("admincategory.html", categories=categories)

def addcategory():
    if request.method == 'POST':
        categoryName = request.form.get('category_name')
        description = request.form.get('description')
        image = request.files.get('category_image')
        
        if not categoryName or not description:
            flash("Please fill name or description", category="caterror")
            return redirect(url_for("addCategory"))
        
        if not image:
            flash("Please fill image field", category="caterror")
            return redirect(url_for("addCategory"))
        
        if image:  
            if not allowed_file(image.filename):
                flash("File type not allowed", category="caterror")
                return redirect(url_for("addCategory"))
        
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            catinfo = Category.query.filter_by(cat_name=categoryName).first()
            if catinfo:
                flash("Category already exists", category="caterror")
                return redirect(url_for("addCategory"))
            
            new_category = Category(
                cat_name=categoryName,
                cat_description=description,
                cat_image=filename,
            )
            db.session.add(new_category)
            db.session.commit()
        
            flash('Category Added Successfully', category="catsuccess")
        return redirect(url_for("addCategory"))
    
    return render_template("adminaddcategory.html")


def deletecategory(catid):
    deletecategory = Category.query.get(catid)
    
    try:
        if deletecategory: 
            complaints = Complaints.query.filter_by(category_id=catid)
            for complaint in complaints:
                db.session.delete(complaint)
                db.session.commit()
                
            db.session.delete(deletecategory)
            db.session.commit()
            
        return render_template("admincategory.html", categories=Category.query.all())
        
    except Exception as e:
        return print(f'error str({e})')


def viewstudent():
    students = Student.query.all()
    return render_template("adminstudent.html", students=students)


def deletestudent(stid):
    deletestudent = Student.query.get(stid)
    
    try:
        if deletestudent:
            complaints = Complaints.query.filter_by(student_id=stid)
            for complaint in complaints:
                db.session.delete(complaint)
                db.session.commit()
            
            db.session.delete(deletestudent)
            db.session.commit()
            
        return render_template("adminstudent.html", students=Student.query.all())
        
    except Exception as e:
        return print(f'error str({e})')
    
    
def viewcomplaints():
    complaints = Complaints.query.all()
    allstudents = Student.query.all()
    allcategories = Category.query.all()
    students = {student.id: {'name': student.student_name, 'year': student.student_year, 'major': student.student_major} for student in allstudents}
    categories = {category.id: category.cat_name for category in allcategories}

    return render_template("admincomplaint.html", complaints=complaints, students=students, categories=categories)
    
    
    
def changestate(cid):
    complaint = Complaints.query.get(cid)

    if request.method == 'POST':
        state = request.form.get('state')

        if not state:
            return jsonify(success=False, message='Require to choose state')
        try:
            complaint.status = state
            db.session.commit()
            
            return jsonify(success=True, redirect=url_for('viewComplaints'))
        except Exception as e:
            return jsonify(success=False, message=f'Server error {e}')
    
def adminprofile():
    user_id = session.get('admin_id')
    admin = Admin.query.get(user_id)
     
    if request.method == 'POST':
        if 'profileImage' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['profileImage']
        
        if file:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                admin.admin_image = filename
                db.session.commit()
                
                admin = Admin.query.filter_by(id=user_id).first()
                myadmin = {
                            "admin_id": admin.id,
                            "admin_name": admin.admin_name,
                            "admin_email": admin.admin_email,
                            "admin_profile": admin.admin_image,
                        }
                session['admin'] = myadmin
                print("successfully uploaded")
                return redirect(url_for('adminProfile'))

    return render_template('adminprofile.html', user=admin)

def updateadmininformation():
    user_id = session.get('admin_id')
    admin = Admin.query.get(user_id)
    
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get('email')
        phone = request.form.get("phone")
        
        if len(email) < 5:
            flash('Invaild email', category='error')
        elif len(name) < 2:
            flash('Name must be longer than 2 letters', category='error')
        elif len(phone) < 5:
            flash('Phone Number must be longer than 5 letters', category='error')
        else:
            admin.admin_name = name
            admin.admin_email = email
            admin.admin_phone = phone
            db.session.commit()
            admin = Admin.query.filter_by(id=user_id).first()
            myadmin = {
                        "admin_id": admin.id,
                        "admin_name": admin.admin_name,
                        "admin_email": admin.admin_email,
                        "admin_profile": admin.admin_image,
                    }
            session['admin'] = myadmin
            print("update successfully")
            return redirect(url_for('adminProfile'))
        
        return render_template('adminprofile.html', user=admin)