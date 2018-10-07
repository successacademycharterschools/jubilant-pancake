function show_result(result) {
    $("#result").text(result);
}

function do_submit() {
    let src = "editd/" + $("#source").val() + "/" + $("#target").val();
    console.log("Getting: " + src);
    $.ajax(src, {
        success: show_result
    });
}

$(function() {
    $("#submit").on("click", do_submit);
});
