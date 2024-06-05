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
