// Sample script demonstrating a simple Map/Reduce calculation of monthly profits
// similar situations could exploit parallel processing

const sales = require('./sales.json')

console.log("Dati di partenza: ");
console.log(sales);

// Defines what to do on item passed as a parameter 
let funzione = function(item) {
        return {
                key: item.year + "-" + item.month, value: item.value
        }
};

// Sample execution with one ojbect only
// let dato = { year: 2020, month: 12, value: 10, altro: "Ciao"};
// let x = funzione(dato)
// console.log(x);

// Map Function - Returns interesting pieces of information only
const temp = sales.map(funzione);

// sales.map(funzione) is somewhat similar to:
// foreach (elemento in map) { 
//	funzione(elemento)
//}

console.log("Risultato del mapping:");
console.log(temp);

console.log("Esecuzione del reduce");

// Reduce function - Actually makes calculations
const iterate = temp.reduce((results, item, index) => {
 	console.log("Elemento " + index + item.key + ": " + item.value);
	console.log(results);
	if (typeof results[item.key] == 'undefined') {
  		results[item.key] = 0;
  	}
  	results[item.key] += item.value;
  	return results;
}, []);

console.log("Risultato finale");
console.log(iterate);
