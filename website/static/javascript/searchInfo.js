function searchInfo(){
    searchInput = document.getElementById('searchInput').value;
    searchfunction(searchInput)
}

function searchfunction(searchInput) {
    $("#search-table-body tr").each(function() {
        var findingvalue = $(this).find(".searchedvalue").text().toLowerCase();
        if (findingvalue.includes(searchInput.toLowerCase())){
            $(this).show();
        }else{
            $(this).hide();
        }
    });
}