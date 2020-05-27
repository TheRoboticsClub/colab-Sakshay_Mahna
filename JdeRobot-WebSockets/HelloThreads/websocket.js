//Editor Part
var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");

// Image Part
var canvas = document.getElementById("gui_canvas"),
    context = canvas.getContext('2d');
    image = new Image();

image.onload = function(){
    context.drawImage(image, 0, 0);
}

//WebSocket for Code
var websocket_code = new WebSocket("ws://127.0.0.1:1905/");

websocket_code.onopen = function(event){
    alert("[open][code] Connection established!");
}
websocket_code.onclose = function(event){
    if(event.wasClean){
        alert(`[close][code] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    }
    else{
        alert("[close][code] Connection closed!");
    }
}

// WebSocket for Image
var websocket_image = null;

// Function to initialize websocket_image settings!
function initialize_image_websocket(){
    websocket_image.onopen = function(event){
        alert("[open][image] Connection established!");
    }

    websocket_image.onclose = function(event){
        if(event.wasClean){
            alert(`[close][image] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        }
        else{
            alert("[close][image] Connection closed!");
        }
    }

    // What to do when a message from server is received?
    websocket_image.onmessage = function(event){
        var data = JSON.parse(event.data),
            source = decode_utf8(data.image),
            shape = data.shape;

        canvas.width = shape[1];
        canvas.height = shape[0];

        image.src = "data:image/jpeg;base64," + source;

        websocket_image.send("Image Displayed!")
    };
}


// To decode the image string we will receive from server
function decode_utf8(s){
    return decodeURIComponent(escape(s))
}

// Function that sends/submits the code!
function submitCode(){
    var python_code = editor.getValue();
    console.log("Code Sent! Check terminal for more information!");
    websocket_code.send(python_code);

    if(websocket_image != null){
        websocket_image.close();
    }

    websocket_image = new WebSocket('ws://127.0.0.1:2303/');
    initialize_image_websocket();
}