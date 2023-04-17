// Team DJ :: Joseph Jeon, Daniel Yentin  
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
      console.log(items[i].classList)
    if (i%2==0){
      items[i].classList.remove('blue');
      items[i].classList.remove('green');
      items[i].classList.add('red');
    } else {
      items[i].classList.remove('red');
      items[i].classList.remove('green');
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB

var fib = function(n){
  if (n < 2) return n;
  return fib(n - 2) + fib(n - 1);
};

// FAC

var fac = function(n){
  if (n < 2) return 1;
  return n * fac(n - 1);
};

// GCD

var gcd = (a, b) => {
  if (a < b){
    [a,b] = [b,a];
  }
  if (a % b == 0){
    return b;
  } else{
    return gcd(b, a % b);
  }
};

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};


