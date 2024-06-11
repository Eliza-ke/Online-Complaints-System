$(document).ready(function () {
  $("#changePasswordForm").submit(function (event) {
    event.preventDefault();

    var stid = $("#stid").val();
    var oldpassword = $("#oldpassword").val();
    var password1 = $("#password1").val();
    var password2 = $("#password2").val();

    $.ajax({
      type: "POST",
      url: "/changePassword",
      data: {
        stid: stid,
        oldpassword: oldpassword,
        password1: password1,
        password2: password2,
      },
      success: function (response) {
        console.log("successful: ", response.message);
        if (response.success) {
          modalalert(response.message);
        } else {
          document.getElementById("showerror").textContent = response.message;
        }
      },
      error: function (xhr, status, error) {
        console.log("failed in ajax function:" + error);
      },
    });
  });


document.querySelector("#backHome").onclick = function () {
    window.location.href = "/";
  };

});

function modalalert(message) {
  document.getElementById("showMessage").textContent = message;
  document.getElementById("myModalalert").style.display = "block";
}

