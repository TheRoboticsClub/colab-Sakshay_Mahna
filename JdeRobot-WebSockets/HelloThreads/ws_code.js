//Editor Part
var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");

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
}