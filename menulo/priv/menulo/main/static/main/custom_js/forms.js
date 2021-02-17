$(document).on('submit','#guest-form', function(){
$.ajax({ 
    type: $(this).attr('method'), 
    url: this.action, 
    data: $(this).serialize(),
    context: this,
    success: function(data, status) {
        document.getElementById("guest-form").reset();
        document.getElementById('guest_message').style.visibility = 'visible'
    }
    });
    return false;
});