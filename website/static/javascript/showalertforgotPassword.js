$(document).ready(function () {
    $("#forgotPasswordForm").submit(function (event) {
      event.preventDefault();
  
      var name = $("#name").val();
      var email = $("#email").val();
      var reason = $("#reason").val();

      $.ajax({
        type: "POST",
        url: "/forgotPassword",
        data: {
          name: name,
          email: email,
          reason: reason,
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
  
  document.querySelector("#closesubmittedalert").onclick = function () {
      document.getElementById("myModalsubmittedalert").style.display = "none";
    };
  
  document.querySelector("#backHome").onclick = function () {
      window.location.href = "/";
    };
  
  });
  
  function modalalert(message) {
    document.getElementById("showMessage").textContent = message;
    document.getElementById("myModalsubmittedalert").style.display = "block";
  
  
  }
  
  