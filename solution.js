// Sample script demonstrating a simple Map/Reduce calculation of monthly profits
// similar situations could exploit parallel processing
const sales = require('./sales.json')

// Map Function - Returns interesting pieces of information only
const temp = sales.map(function(item) {
	return {
		key: item.year + "-" + item.month, value: item.value
	}
});

// Reduce function - Actually makes calculations
const results = [];
const iterate = temp.reduce((total, item, index, array) => {
  	if (typeof results[item.key] == 'undefined') {
  		results[item.key] = 0;
  	}
  	results[item.key] += item.value;
  	return results;
}, 0);

console.log(results);