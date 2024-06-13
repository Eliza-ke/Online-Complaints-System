from sqlalchemy.sql import func
from website.web_config import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(255), nullable=False)
    cat_description = db.Column(db.String(255), nullable=False)
    cat_image = db.Column(db.String(255), nullable=False)
    complaints = db.relationship('Complaints')

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(255), nullable=False)
    admin_email = db.Column(db.String(255), nullable=False)
    admin_phone = db.Column(db.String(255), nullable=False)
    admin_password = db.Column(db.String(255), nullable=False)
    admin_image = db.Column(db.String(255), nullable=False)
    
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255), nullable=False)
    student_email = db.Column(db.String(255), nullable=False)
    student_password = db.Column(db.String(255), nullable=False)
    student_image = db.Column(db.String(255), nullable=False)
    student_year = db.Column(db.String(255), nullable=False)
    student_major = db.Column(db.String(255), nullable=False)
    student_phone = db.Column(db.String(255), nullable=False)
    complaints = db.relationship('Complaints')
    

class Complaints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complaint_letter = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    
    
class ForgotPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(255),nullable=False)
    contact_email = db.Column(db.String(255), nullable=False)
    contact_message = db.Column(db.String(255),nullable=False)