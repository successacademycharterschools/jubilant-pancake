function editDistance() {
  var data = JSON.stringify({
    word1: $('#word1').val(), 
    word2: $('#word2').val()
  });

  var params = {
    method: 'POST', 
    url: '/edit_distance', 
    contentType: 'application/json', 
    dataType: 'json', 
    data: data
  };

  $.ajax(params).done(function(resp) {
    $('#result').attr('class', 'alert alert-success');
    var text = '"' + resp.word1 + '" vs. "' + resp.word2 + '" = ' + resp.edit_distance; 
    $('#resultText').text(text);
  }).fail(function(resp) {
    $('#result').attr('class', 'alert alert-danger');
    var responseText = JSON.parse(resp.responseText);
    $('#resultText').text(responseText.message);
  });
}

$(document).ready(function() {
  $('#distanceForm').submit(function(e) {
    e.preventDefault();
    editDistance();
  });
});
