//Editor Part
var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");

var stop_button = document.getElementById("stop");
stop_button.disabled = true;
stop_button.style.opacity = "0.4";
stop_button.style.cursor = "not-allowed";

//WebSocket for Code
var websocket_code = new WebSocket("ws://127.0.0.1:1905/");

websocket_code.onopen = function(event){
    alert("[open] Connection established!");
}
websocket_code.onclose = function(event){
    if(event.wasClean){
        alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    }
    else{
        alert("[close] Connection closed!");
    }
}

// Function that sends/submits the code!
function submitCode(){
    var python_code = editor.getValue();
    console.log("Code Sent! Check terminal for more information!");
    websocket_code.send(python_code);

    stop_button.disabled = false;
    stop_button.style.opacity = "1.0";
    stop_button.style.cursor = "default";
}

// Function that send/submits an empty string
function stopCode(){
    var stop_code = "";
    console.log("Message sent!");
    websocket_code.send(stop_code);
}