// To decode the image string we will receive from server
function decode_utf8(s){
    return decodeURIComponent(escape(s))
}

// Websocket and other variables for image display
var websocket = new WebSocket('ws://127.0.0.1:2303/'),
    canvas = document.getElementById("gui_canvas"),
    context = canvas.getContext('2d');
    image = new Image();

websocket.onopen = function(event){
    alert("[open] Connection established!");
}

websocket.onclose = function(event){
    if(event.wasClean){
        alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    }
    else{
        alert("[close] Connection closed!");
    }
}

// For image object
image.onload = function(){
    context.drawImage(image, 0, 0);
}

// What to do when a message from server is received?
websocket.onmessage = function(event){
    var data = JSON.parse(event.data),
        source = decode_utf8(data.image),
        shape = data.shape;

    canvas.width = shape[1];
    canvas.height = shape[0];

    image.src = "data:image/jpeg;base64," + source;

    websocket.send("Image Displayed!")
};
