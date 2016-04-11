$(function() {
    $('#input_1').val('');
    $('#input_2').val('');
    var submit_btn = $('.submit');
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
                alert('An error has occured');
            }
        })
        return false;
    });
});