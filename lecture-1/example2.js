// Simple script to calculate average body temperature for ill people (those with high temperature & sore throat)
// Healthy folks are discarded within reduce operation

const population = require('./population.json')

// Map Function - Returns interesting pieces of information
const temp = population.map(function(item) {
  return [ item.soreThroat, item.temperature ]
});

let selected = 0;

const avg = population.reduce(function (result, item, index, values) {
  if (item.soreThroat && item.temperature > 37) {
      console.log(item);
      selected++;
      result += item.temperature;
  }
  if (index == values.length -1) {
      result = result / selected;
    }
  return result;
}, 0);

console.log(avg);
