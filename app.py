from flask import render_template, redirect, session, url_for
from website.adminfeatures import addcategory, admindashboard, adminprofile, changestate, deletecategory, deletestudent, filtercategory, filterstatus, resetpassword, updateadmininformation, updatecategory, viewcategory, viewcomplaints, viewresetpassword, viewstudent
from website.auth import forgotpassword, signin, signup
from website.clientfeatures import changepassword, clientprofile, oldpassword, send_complaint, updateclientinformation
from website.web_config import create_app

app = create_app()

@app.route('/', methods=['GET','POST'])
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

@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    return forgotpassword()


@app.route('/complaint_form', methods=['GET', 'POST'])
def com_send_message():
    if 'student_id' in session:
        return send_complaint()
    else:
        return redirect(url_for('SignIn'))

@app.route('/oldPassword', methods=['GET', 'POST'])
def oldPassword():
    if 'student_id' in session:
        return oldpassword()
    else:
        return redirect(url_for('SignIn'))
    
@app.route('/changePassword', methods=['GET', 'POST'])
def changePassword():
    if 'student_id' in session:
        return changepassword()
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
    
    
@app.route('/updateCategory/<int:catid>', methods=['GET', 'POST'])
def updateCategory(catid):
    if 'admin_id' not in session:
        return redirect(url_for('home'))
    else:
        return updatecategory(catid)
    
    
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
    
    
@app.route('/filterStatus/<string:status>', methods=['GET', 'POST'])
def filterStatus(status):
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return filterstatus(status)
    
    
@app.route('/filterCategory/<int:catid>', methods=['GET', 'POST'])
def filterCategory(catid):
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return filtercategory(catid)
    
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
    
@app.route('/viewResetPassword', methods=['GET', 'POST'])
def viewResetPassword():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return viewresetpassword()
    
@app.route('/resetPassword/<int:stid>', methods=['GET', 'POST'])
def resetPassword(stid):
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return resetpassword(stid)
    
    
@app.route('/adminDashboard', methods=['GET', 'POST'])
def adminDashboard():
    if 'admin_id' not in session:
        return redirect(url_for('SignIn'))
    else:
        return admindashboard()
    

    
    
if __name__ == '__main__':
    app.run(debug=True)
