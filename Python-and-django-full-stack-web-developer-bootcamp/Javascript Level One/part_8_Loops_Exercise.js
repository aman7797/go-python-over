/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var n = 0
while(n < 5){
	console.log("hello");
	n++;
}

// For Loop
for(n = 0; n < 5; n++){
	console.log("hello");
}




/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var n = 0
while(n < 25){
	if(n%2!=0){
	console.log(n);
	}
	n++;
}

// METHOD TWO
// For Loop
for ( n = 0; n < 25; n++){
	if(n%2!=0){
		console.log(n);
	}
}