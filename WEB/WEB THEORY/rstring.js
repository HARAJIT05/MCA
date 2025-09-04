const readline = require('readline').createInterface({
input: process.stdin,
output: process.stdout
});
function reverseString(str) {
return str.split('').reverse().join('');
}
readline.question('Enter a string: ', (input) => {
const reversed = reverseString(input);
console.log(reversed);
readline.close();
});