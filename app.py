from flask import render_template, redirect, session, url_for
from website.adminfeatures import addcategory, adminprofile, changestate, deletecategory, deletestudent, updateadmininformation, viewcategory, viewcomplaints, viewstudent
from website.auth import signin, signup
from website.clientfeatures import clientprofile, send_complaint, updateclientinformation
from website.web_config import create_app

app = create_app()

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template("homepage.html")

@app.route('/sign_up', methods=['GET','POST'])
def Signup():
    return signup()

@app.route('/sign_in', methods=['GET','POST'])
def SignIn():
    return signin()

@app.route('/sign_out')
def Signout():
    session.pop('student_id', None)
    session.pop('admin', None)
    session.pop('admin_id', None)
    return redirect(url_for('SignIn'))

@app.route('/complaint_form', methods=['GET', 'POST'])
def com_send_message():
    if 'student_id' in session or 'admin_id' in session:
        return send_complaint()
    else:
        return redirect(url_for('SignIn'))
    
@app.route('/profile', methods=['GET', 'POST'])
def clientProfile():
    if 'student_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return clientprofile()
    
@app.route('/updateclientInfo', methods=['GET', 'POST'])
def updateclientInfo():
    if 'student_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return updateclientinformation()
    
# admin
@app.route('/viewCategory', methods=['GET', 'POST'])
def viewCategory():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return viewcategory()
    
@app.route('/addCategory', methods=['GET', 'POST'])
def addCategory():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return addcategory()
    
# @app.route('/updateCategory/<int:catid>', methods=['GET', 'POST'])
# def updateCategory(catid):
#     if 'admin_id' not in session:
#         return redirect(url_for('home'))
#     else:
#         return updatecategory(catid)
    
    
@app.route('/deleteCategory/<int:catid>', methods=['GET', 'POST'])
def deleteCategory(catid):
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return deletecategory(catid)

@app.route('/viewStudent', methods=['GET', 'POST'])
def viewStudent():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return viewstudent()

@app.route('/deleteStudent/<int:stid>', methods=['GET', 'POST'])
def deleteStudent(stid):
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return deletestudent(stid)
    
    
@app.route('/viewComplaints', methods=['GET', 'POST'])
def viewComplaints():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return viewcomplaints()
    
    
@app.route('/changeState/<int:cid>', methods=['GET', 'POST'])
def changeState(cid):
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return changestate(cid)

@app.route('/adminProfile', methods=['GET', 'POST'])
def adminProfile():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return adminprofile()
    
@app.route('/updateAdminInfo', methods=['GET', 'POST'])
def updateAdminInfo():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return updateadmininformation()
    
    
    
if __name__ == '__main__':
    app.run(debug=True)