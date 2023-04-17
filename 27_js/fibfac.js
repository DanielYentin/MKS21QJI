// Team DJ :: Joseph Jeon, Daniel Yentin 
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------

// as a duo...
// pair programming style,
// implement a fact and fib fxn

function fact(n){
	if (n < 2) return 1;
	return n * fact(n - 1)
}

function fib(n){
	if (n < 2) return n;
	return fib(n - 2) + fib(n - 1)
}

/*
function fib_funny(n){
	return parseInt((Math.pow((1 + Math.sqrt(5)) / 2, n) - Math.pow((1 - Math.sqrt(5)) / 2, n))/Math.sqrt(5))
}
*/

function test(){
	console.log("Factorial test")
	for (var i = 0; i < 10; i++) {
		console.log(fact(i))
	}
	console.log("Fibonacci test")
	for (var i = 0; i < 10; i++) {
		console.log(fib(i))
	}
	/*
	console.log("Fibonacci test (funny)")
	for (var i = 0; i < 100; i++) {
		console.log(fib_funny(i))
	}
	*/
}

test()

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
