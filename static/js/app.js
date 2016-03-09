function calcDistance() {
  $.ajax({
    url: '/api/v1/distance',
    method: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify({first: $('#first').val(), second: $('#second').val()})
    })
    .done(function(resp) {
      $('#result').attr('class', 'alert alert-success');
      $('#response').text('Edit distance = ' + resp.distance);
    })
    .fail(function(resp) {
      $('#result').attr('class', 'alert alert-danger');
      var payload = JSON.parse(resp.responseText);
      $('#response').text('Error occured: ' + payload.error);
    })
    .always(function(resp) {
      $('#calcButton').button('reset')
    });
}

$(document).ready(function() {
  $('#calcButton').on('click', function () {
    var $btn = $(this).button('loading')
    calcDistance();
  })
});
