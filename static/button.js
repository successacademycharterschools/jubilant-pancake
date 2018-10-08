function show_result(result) {
    $("#result").text(result);
}

function do_submit() {
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
