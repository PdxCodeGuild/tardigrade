const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()><?/'`:;"
const code = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM0123456789!@#$%^&*()><?/'`:;"
let inputs = prompt("Enter your string to cipher")
let num_input = prompt("Enter rotation number")
let num = parseInt(num_input);
let cipher = " ";
for (let i = 0; i < inputs.length; i++) {
    let index = alphabet.indexOf(inputs[i]);
    cipher += code[index + num];
}

console.log('Orginal Input', inputs)
console.log('New Cipher', cipher)
console.log('Rotation', num)