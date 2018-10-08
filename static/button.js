function show_result(result) {
    // Display the result in the #result span
    $("#result").text(result);
}

function do_submit() {
    // Submit the source and target to the server, await response
    $("#result").text("");
    $.ajax('editd', {
        data: {
            source: $("#source").val(),
            target: $("#target").val()
        },
        success: show_result
    });
}

$(function() {
    $("#submit").on("click", do_submit);
});
