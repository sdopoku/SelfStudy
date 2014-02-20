//Create a Car Object using JS Prototype inheritance
/*
1) Create the prototype Object
2) Define object function
3) Let object inherit prototype
4) Use object with inherited prototype to create new objects

*/

var carPrototype = {
	manufacturer : "BMW",
	model : "3 series",
	year : 2014,
	colour : "red",
	rating : 9
} 


function Car(manufacturer){
	this.manufacturer = manufacturer;
} 

Car.prototype  = carPrototype;
