let student_id;

function deleteStudent(stid) {
    student_id = stid
    document.getElementById('myModaldeleteStudent').style.display = 'block';
}
document.querySelector('.closedeleteStudent').onclick = function() {
    document.getElementById('myModaldeleteStudent').style.display = 'none';
}

document.getElementById('cancelDeleteStudent').onclick = function() {
    document.getElementById('myModaldeleteStudent').style.display = 'none';
}

document.getElementById('confirmDeleteStudent').onclick = function() {
    document.getElementById('myModaldeleteStudent').style.display = 'none';
    window.location.href = '/deleteStudent/'+student_id;
}