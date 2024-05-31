let idvalue = "";
function updatecategory(element) {
    idvalue = element.getAttribute("data-id-value");
    let categoryName = element.closest("tr").querySelector("td:first-child").textContent;
    let categoryDescription = element.closest("tr").querySelector("td:nth-child(2)").textContent;
    let categoryImageSrc = element.closest("tr").querySelector("td:nth-child(3) img").src;
    
    $("#updateCategoryName").val(categoryName);
    $("#updateCategoryDes").val(categoryDescription);
    $("#updateCategoryImagePreview").attr("src", categoryImageSrc);
    
    document.getElementById("myModalAdminCategory").style.display = "block";
    
    $(".closeCategory").click(function () {
        document.getElementById("myModalAdminCategory").style.display = "none";
    });
}

// let file ="";
// document.getElementById('updateCategoryImage').addEventListener('change', function(event) {
//      file = event.target.files[0];
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             document.getElementById('updateCategoryImagePreview').src = e.target.result;
//             // Store base64 string in a hidden input field for form submission
//             document.getElementById('updateCategoryImageBase64').value = e.target.result;
//         };
//         reader.readAsDataURL(file);
//     }
// });

// document.getElementById('editCategoryForm').addEventListener('submit', function(event) {
//     event.preventDefault(); // Prevent default form submission

//     const form = document.getElementById('editCategoryForm');
//     const formData = new FormData(form);

//     fetch('/upload', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Success:', data);
//         window.location.href= response.redirect;
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//         alert(message)
//     });
// });

// // preview
// document.getElementById('updateCategoryImage').addEventListener('change', function(event) {
//     const file = event.target.files[0];
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             document.getElementById('updateCategoryImagePreview').src = e.target.result;
//         }
//         reader.readAsDataURL(file);
//     }
// });


function deleteCategory(catid) {
    document.getElementById('myModaldeleteCategory').style.display = 'block';

    document.querySelector('.closedeleteCategory').onclick = function() {
        document.getElementById('myModaldeleteCategory').style.display = 'none';
    }

    document.getElementById('cancelDelete').onclick = function() {
        document.getElementById('myModaldeleteCategory').style.display = 'none';
    }

    document.getElementById('confirmDelete').onclick = function() {
        document.getElementById('myModaldeleteCategory').style.display = 'none';
        window.location.href = '/deleteCategory/'+catid;
    }
}
