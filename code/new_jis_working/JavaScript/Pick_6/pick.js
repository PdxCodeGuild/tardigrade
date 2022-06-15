// a ticket costs $2
// if 1 number matches, you win $4
// if 2 numbers match, you win $7
// if 3 numbers match, you win $100
// if 4 numbers match, you win $50,000
// if 5 numbers match, you win $1,000,000
// if 6 numbers match, you win $25,000,000
// One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

// Steps
// Generate a list of 6 random numbers representing the winning tickets
// Start your balance at 0
// Loop 100,000 times, for each loop:
// Generate a list of 6 random numbers representing the ticket
// Subtract 2 from your balance (you bought a ticket)
// Find how many numbers match
// Add to your balance the winnings from your matches
// After the loop, print the final balance

function listOfSix() {
  const sixNumbers = []
  
  while (sixNumbers.length < 6) {
    let num = (Math.floor(Math.random() * 99) + 1)
    sixNumbers.push(num)
  }
  return sixNumbers
   
  }

function matchedNum() {
  let pickedNumber =  listOfSix()
  let ticketNumber =  listOfSix()
  let matchedNums = []
  let indexA = 0

  while(indexA < pickedNumber.length) {
    let numA = pickedNumber[indexA]
    let numB = ticketNumber[indexA]

    if(numA === numB){
      matchedNums.push(numA)
    }
    indexA +=1
  }
  return matchedNums.length

}

function winningCalc(){
  let totalMatches = matchedNum()
  const payOut = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
  }

  let netTotal = (payOut[totalMatches]) - 2
  return netTotal

}

const oneHundredThousand = []

while(oneHundredThousand.length<100000){
  let profit = winningCalc()
  oneHundredThousand.push(profit)
}

function sumArray(array) {
  let sum = 0;

  array.forEach(item => {
    sum += item;
  });
  return sum;
}

let soulutionVar = sumArray(oneHundredThousand)


console.log("Your total winning is " +  soulutionVar)

// Version 2 ROI

let ROI = (soulutionVar-200000)/200000

console.log("Your return on investment is " +  ROI)





  
  
