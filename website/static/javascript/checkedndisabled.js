$('#agree').click(function(){
    if ($(this).is(':checked')){
        $('#submitcomplaint').removeAttr('disabled');
    }else {
        $('#submitcomplaint').attr('disabled', 'disabled');
    }
})