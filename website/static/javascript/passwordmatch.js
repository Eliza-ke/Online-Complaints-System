function passwordMatch(){
    password1 = document.getElementById('password1').value;
    password2 = document.getElementById('password2').value;
    console.log(password1)
    
    if (password1 != password2){
        document.getElementById("passwordError").innerHTML = "*** Your password does not match";
    }else if (password1 == password2){
        document.getElementById("passwordError").innerHTML = "";
    }
}