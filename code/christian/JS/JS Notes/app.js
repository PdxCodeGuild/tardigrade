// console.log('hello world')
// -------------------------------------------------------------
// NOTES: JS gives NO 'F's about syntax... you need to be careful
// for (let i = 0; i < 5; i++

//     ) {
//     console.log(

//         i)
// }
// -------------------------------------------------------------
// MOTES: Variables must be declared with 'let' or 'const'
// 'let' means that a variable can be changed over time, as overwritten below
// 'constant' will raise "TypeError: Assignment to constant variable" if you try to overwrite

// let dog = 'woof woof'
// const cat = 'meeeow'

// dog = 'I am now a caterpillar'
// console.log(dog)

// cat = 'I am now a caterpillar'
// console.log(cat)

// -------------------------------------------------------------
// NOTES: const brakes the code because 'i' will never go past '0'

// for (let i = 0; i < 5; i++) { console.log(i) }
// for (const i = 0; i < 5; i++) { console.log(i) }

// -------------------------------------------------------------
// NOTES: CamelCase
// SCOPE = const, let, vs VAR
// since a recent update, VAR is rarely used. VAR can be renamed like let,
// and the scope is more extended

// let schoolBoy = 'hello'
// const blackCat = 'meeeeeeow'
// var randomVariable = 23;

// N- The below code brakes at const y because const y is not global,
// N- The definition dies within the if statement

// if (2<10){
//     var x = 10
//     const y = 11
// }

// console.log(x)
// console.log(y)

// NOTES: This code fises it

// if (2<10){
//     var x = 10
//     var y = 11
// }

// console.log(x)
// console.log(y)

// -------------------------------------------------------------

// for (let i = 0; i < 10; i++){
//     console.log(i)
// }
// -------------------------------------------------------------
// NOTES: 'const' can preserve your data, such as in lists

// const myArray = [1, 2, 3, 4]

// myArray.push(3)

// console.log(myArray)

// -------------------------------------------------------------

// const a = 5; //number
// const b = 10.4 //number
// const c = 'hello there' //string
// const d = true //Boolean
// const e = null //null
// const f = undefined //undefined

// console.log(typeof (b))
// -------------------------------------------------------------
// // NOTES: Arrays are lists in Python

// const thisIsAnArray = [1, 2, 3, 4]
// console.log(thisIsAnArray[0])
// console.log(thisIsAnArray[3])
// thisIsAnArray.push(5)

// -------------------------------------------------------------
// // NOTES: 'Objets' are dictionaries in Python

// const person = {
//     firstName: 'Christian',
//     lastName : 'Eberhardt',
//     age: 33
// }

// console.log(person['firstName'])
// -------------------------------------------------------------
// NOTES: parseInt will remove the float
// const x = parseInt('4.2')
// console.log(x)
// console.log(typeof(x))

// // NOTES: parseFloat will preserve the float
// const y = parseFloat('4.2')
// console.log(y)
// console.log(typeof(y))

// // NOTES: Convert to string (has to be done with 'let')
// let z = 5
// z = z.toString()
// console.log(typeof(z))

// -------------------------------------------------------------
// NOTES: input from user

// const name = prompt('Tell me your name!')

// alert("Hello " + name + ".")

// -------------------------------------------------------------

// const myNumber = parseInt(prompt("Type a number: "))
// alert("Number chosen is " + myNumber + ".")
// -------------------------------------------------------------
// NOTES: Want to increment a number in JS? Use i++. It's like a built-in counter

// a = 1
// a++
// alert(a)
// -------------------------------------------------------------
// const j = 1
// const k = 1

// console.log(j>k)
// console.log(j===k)
// console.log(j!==k)

// -------------------------------------------------------------
// const temperature = 56;
// if (temperature < 60) {
//     alert('cold')
// }
// else if (temperature < 80) {
//     alert('warm')
// }
// else { alert('hot') }

// -------------------------------------------------------------
// NOTES: 0 = false, 1 = true

// let k = 0

// console.log(Boolean(0))

// ==================DAY 2 NOTES================================
// const x = 6
// // Top left of keyboard
// let myString = `My number is ${x}`
// //When using console, 'myString' will return the statement above

// -------------------------------------------------------------

// function getFullName(title, fname, lname, degree){
//     return `The full info is ${title} ${fname} ${lname} ${degree}`
// }

// console.log(getFullName('Mr.', 'Christian', 'Eberhardt', 'EMER'))

// -------------------------------------------------------------

// const myValues = [0, 1, 2, 3]

// for (let i =0; )

// -------------------------------------------------------------
// // The colon betwen a and b is an otherwise statement

// function minValue(a,b){
//     return (a<b) ? a : b
// }

// console.log(minValue(5, 3))
// console.log(minValue(1, 10))


// -------------------------------------------------------------
// // HOQ ro ITERATE through OBJECTS:

// for (let property in libraryUser){
//     console.log(key, libraryUssser[key])
// }
// -------------------------------------------------------------
// // Array and Loops

// const myList = [1, 2, 3, 4]
// const myString = 'hello there'

// console.log(myList[0])

// // for (let i = 0; i < myList.length; i++) {
// //     console.log(i, myList[i])
// // }

// for (let i = 0; i < myString.length; i++) {
//     console.log(i, myString[i])
// }

// for (let i = 0;  i < 5; i++){
//     console.log(i)
// }

// for (let i = 5;  i >= 0; i--){
//     console.log(i)
// }

// // WHILE LOOPS

// let i = 0
// while (i < 10) {
//     console.log('hello')
//     i++
// }
// -------------------------------------------------------------
// // ANAGRAM

// let word = 'public relations'
// let anagram = 'crap built on lies'

// function checkAnagram(word, anagram) {
//     //sort the letter
//     //remove spacing
//     //compare them
//     word = word.replace(' ', '')
//     word = word.split('').sort().join().trim()
//     anagram = anagram.split('').sort().join().trim()
//     console.log(word)
//     console.log(anagram)
//     if (word == anagram) {
//         return true
//     } else {
//         return false
//     }
// }

// console.log(checkAnagram(word, anagram))
//=======================DAY 3==================================
// // For loops work well for strings and arrays

// const myArray = ['a', 'b', 'c', 'd']
// const myString = 'hello there'

// for (let i=0; i<myString.length; i ++){
//     console.log(myString[i])
// }


// for (let i = 0; i < 6; i++) {
//     console.log(i)
// }

// // // Alerts will work in browsers (there built for it) but not in the cmd line
// alert("What up, yo!")
// -------------------------------------------------------------

// // In JS you cannot use the [-1] trick for arrays

// const nestedObjectArray = [1, 2, 3, ['a', 'b', 'c']]

// console.log(nestedObjectArray[1])

// // In source/console, you can type the following:
// // nestedObjectArray[03][01]
// -------------------------------------------------------------

// const nestedObjectArray = [

//     {
//         firstName: 'Christian',
//         lastName: 'E',
//         hobbies: ['golf', 'food']
//     },

//     {
//         firstName: 'Nancy',
//         lastName: 'E',
//         hobbies: ['shopping', 'food']
//     }
// ]

// for (let i = 0; i < nestedObjectArray.length; i++) {
//     let elementInsideArray = nestedObjectArray[i].hobbies;
//     for (let j = 0; j < elementInsideArray.length; j++){
//         console.log(elementInsideArray[j])
//     }
//     console.log(elementInsideArray)
// }

// -------------------------------------------------------------
// // ARRAYS

// function hello(){
//     console.log('hello there')
// }

// const myArrayTwo = [1, 7.7, 'hello', null, undefined, NaN, "", hello()]

// // // add something

// // // pus to push something to the top
// // // unshift to push something at the beginning
// // // pop to remove something at the top
// // // shift to remove something at the beginning

// myArrayTwo.push('7')
// myArrayTwo.pop()
// myArrayTwo.unshift(0)

// -------------------------------------------------------------
// // Rotate an array in place
// let nums = [1, 2, 3, 4, 5]

// //COPY AND PASTED IN SNIPPITS
// function rotate(k){
// for (let i =0; i < nums.length; i++){
//     nums.unshift(nums.pop)
// }

// for (const num of nums){
//     console.log(num)
// }

// -------------------------------------------------------------
// // SWAP ELEMENTS IN AN ARRAY

// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------

// ===========================DAY 4=============================
/// CHALLENGE - Find biggest number
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max
// Iterate through array
// Track current numbers
// Have a global counter
// Compare current number to global counter

// const myNumbers = [1, 2, 3, 101, 10, 55]

// function calculateBiggest() {
//     let currentNum
//     let globalCounter = 0
//     for (let i = 0; i < myNumbers.length; i++) {
//         currentNum = myNumbers[i]
//         if (currentNum > globalCounter) {
//             globalCounter = currentNum
//         }
//     }
//     return globalCounter
// }

// console.log(calculateBiggest(myNumbers))

// -------------------------------------------------------------
// // CHALLENGE - Missing Element
// // For loop
// // Compare the two elements
// // Return the missing element

// const arr = [0, 1, 2, 3, 4, 5]
// const shuffled = [4, 5, 0, 1, 2]

// function missingElement(arr, shuffled) {
//     let sortedArr = arr.sort()
//     let sortedShuffled = shuffled.sort()

//     for (let i = 0; i < sortedArr.length; i++) {
//         if (sortedArr[i] != sortedShuffled[i]) {
//             return sortedArr[i]
//         }
//     }
// }

// console.log(missingElement(arr, shuffled))

// -------------------------------------------------------------
/// CHALLENGE - Reverse Word
// You cannot use negative indexes in JS
// Split to convert into an array

const input = 'this is the best'

// // Reverse loop...
// // Unfortunately, this spells it all backwards.
// // We just want the words in reverse order

// for (let i = input.length; i > 0; i--){
//     console.log(input[i])
// }

// // Option Two - THIS IS BROKE, MUST FIX

// function reverseWord(input) {
//     let newString = ''
//     const trimmedWord = input.trim().split(" ")
//     for (let i = trimmedWord.length - 1; i >= 0; i--) {
//         newString += trimmedWord[i] + " "
//         return newString
//     }
// }

//     console.log(reverseWord(input))
// -------------------------------------------------------------
///CHALLENGE -Filtering

const fruits = ["Banana", "Orange", "Apple", "Mango", "Mango", "Mango"]

const newArray = []

// // Option 1: Use set()

// const result = new Set(fruits)
// console.log(result)

// // Option 2: Use indexOf()
// // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new


// // Will review after the break :)
// for  (let i = 0; i < fruits.length; i ++){
//     if (newArray.indexOf(fruits[i] == -1)){
//     newArray.push(fruits[1])
// }
// }

// // Option 3: Use includes
// // NOTICE the use of '!" to indiccate "not included"

// for (let i = 0; i < fruits.length; i++) {
//     if (!(newArray.includes(fruits[i]))) {
//         newArray.push(fruits[i])
//     }
// }

// console.log(newArray)

// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
