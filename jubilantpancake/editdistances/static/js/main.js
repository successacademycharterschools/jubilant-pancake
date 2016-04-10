$(function() {
    var submit_btn = $('.submit');
    $('.submit').on('click', function(){
        var input_1 = $('#input_1').val();
        var input_2 = $('#input_2').val();

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
        return false
    });
});