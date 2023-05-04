var c = document.getElementById('slate');

var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = (e) => {
	console.log("toggling...");
	if(mode == "rect"){
		mode = "circ"
	}
	else{
		mode = "rect"
	}
}

var drawRect = function(e) {
	var rect = c.getBoundingClientRect()
	var mouseX = e.x - rect.left;
	var mouseY = e.y - rect.top;
	console.log("mouseclick registered at ", mouseX, mouseY);
	ctx.fillRect(mouseX, mouseY, 20, 21);
}

var drawCircle = (e) => {
	var rect = c.getBoundingClientRect()
	var mouseX = e.x - rect.left;
	var mouseY = e.y - rect.top;
	console.log("mouseclick registered at ", mouseX, mouseY);
	ctx.beginPath();
	ctx.arc(mouseX, mouseY, 50, 0, Math.PI * 2, true);
	ctx.fillStyle = "red";
	ctx.fill();
	ctx.closePath();
}

var draw = (e) => {
	switch(mode){
		case "rect":
			drawRect(e);
			break;
		case "circ":
			drawCircle(e);
			break;
		default:
			break;
	}
}

var wipeCanvas = (e) => {
	ctx.clearRect(0, 0, 10000, 10000);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);


