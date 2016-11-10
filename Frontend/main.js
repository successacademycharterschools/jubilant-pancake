var http = new XMLHttpRequest();

var url = "http://127.0.0.1:8000/quickstart/calc/";
function calculateDistance(){
    var params = {};
    http.open("POST", url, true);

    params.firstString = document.getElementById('firststring').value;
    params.secondString = document.getElementById('secondstring').value;

    //Send the proper header information along with the request
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            document.getElementById("result").innerHTML = http.responseText;
        }
    }
    http.send(JSON.stringify(params));
}

