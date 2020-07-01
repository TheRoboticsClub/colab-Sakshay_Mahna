// Keep a list of commands
var command_number = 0;

// Get the input field and the div
var command = document.getElementsByClassName("command")[command_number];
var python_console = document.getElementById("Console");

// Get the Console ul
var command_list = document.getElementById("Console").childNodes[1];


// Function to go to next command line
function next_command(){
	// Make the current input readonly
	command.readOnly = true;
	
	// Create and append new list item
	var new_item = document.createElement("li");
	
	var new_terminal = document.createElement("input");
	new_terminal.classList.add("terminal");
	new_terminal.setAttribute("value", ">>");
	
	var new_command = document.createElement("input");
	new_command.classList.add("command");
	
	new_item.appendChild(new_terminal);
	new_item.appendChild(new_command);
	
	command_list.appendChild(new_item);
	
	// Make way for the next terminal input
	command_number = command_number + 1;
	
	// Maintain the content of the console
	if(command_number == 2){
		var command_to_delete = command_list.childNodes[1];
		command_to_delete.remove();
		command_number = 2;
	}
	
	command = document.getElementsByClassName("command")[command_number];
}


// Execute a function when the user releases a key
python_console.addEventListener("keyup", function(event){
	// Enter is pressed
	if(event.keyCode == 13){
		// Prevent Default commands
		event.preventDefault();
		
		// Get the value and send to Python Interpreter
		var console_input = "#cons\n" + command.value;
		websocket_code.send(console_input);
		
		// Call the function
		next_command();
		
		// Focus on the next command
		command.focus();
	}
})

// Execute a function when clicked
python_console.addEventListener("click", function(event){
	// Focus on the input that should current be active
	command.focus();
})
