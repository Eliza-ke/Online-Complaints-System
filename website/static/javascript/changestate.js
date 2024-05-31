let currentcid;
function changeState(cid) {
    currentcid = cid
    document.getElementById('myModalChangeState').style.display = 'block';
}
document.querySelector('.closeChangeState').onclick = function() {
    document.getElementById('myModalChangeState').style.display = 'none';
}
document.querySelector('.cancelstate').onclick = function() {
    document.getElementById('myModalChangeState').style.display = 'none';
}
$(document).ready(function(){
    $("#stateform").submit(function(event){
        event.preventDefault();

        var state = $("#modalstate").val();
        $.ajax({
            type: "POST",
            url: '/changeState/'+currentcid,
            data: {
                state: state
            },
            success: function(response){
                console.log("successful: ", response.message);
                if(response.success){
                    window.location.href = response.redirect;
                }else{
                    document.getElementById('showerror').textContent = response.message
                }
            },
            error: function(xhr, status, error){
                console.log("failed in ajax function:"+error);
            }
        })
    })
})
