var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, 1000, 1000);
};

var radius = 0;
var maxRadius = 250;
var growing = true;

var drawDot = () => {
    clear();

    if (growing && radius+1 > maxRadius) {
        growing = false;
    } else if (!growing && radius-1 < 0) {
        growing = true;
    }

    if (growing) {
        radius++; 
    } else {
        radius--;
    }

    ctx.beginPath();
    ctx.arc(maxRadius, maxRadius, radius, 0, Math.PI*2, true);
    ctx.fill();
    ctx.closePath();

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID)
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);