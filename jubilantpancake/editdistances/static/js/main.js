$(function() {
    $('#input_1').val('');
    $('#input_2').val('');
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var submit_btn = $('.submit');
    var csrftoken = getCookie('csrftoken');
    $('.submit').on('click', function(){
        var input_1 = $.trim($('#input_1').val());
        var input_2 = $.trim($('#input_2').val());
        if(input_1 === "" || input_2 === ""){
            alert('Both fields required');
            return false;
        }

        $.ajax({
            type: "POST",
            url: '/edit_distance/',
            data: {
                'input_1': input_1,
                'input_2': input_2
            },
            dataType: 'json',
            success: function(data){
                $('#edit_distance span').text(data['edit_distance']);
                $('.placeholder').css('visibility', 'visible');
            },
            error: function(data){
                console.log(data);
                alert('An error has occured');
            }
        })
        return false;
    });
});