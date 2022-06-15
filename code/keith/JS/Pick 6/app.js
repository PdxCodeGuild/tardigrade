
function pick6() {    /// this function returns a list of 6 random numbers 
    let winningNumber = []

    for (let i = 0; i < 6; i++) {
        winningNumber.push(Math.floor(Math.random() * (100 - 0 + 1) + 0))
    }

    return winningNumber
}


console.log(pick6())

function player6() {     /// this function also returns me a list of 6 random numbers to be used later in for loop
    let playerNums = []

    for (let i = 0; i < 6; i++) {
        playerNums.push(Math.floor(Math.random() * (100 - 0 + 1) + 0))
    }
    return playerNums
}

console.log(player6())


function matchCheck(firstList, secondList) {   /// this function is checking for matches in the same index postion of the two randomly made number list
    let matchList = []

    for (let i = 0; i < firstList.length; i++) {
        
        if (firstList[i] === secondList[i]){
            matchList.push(firstList[i])}
        
        }
        return matchList 
    }


let moneyBalance = 0 
let plays = 100000

for (let i=0; i<plays; i++){
    let counter = 0 
    let money = 0 
    let playersTicket = player6()
    console.log('These are your lotto numbers', playersTicket);
    let winningTicket = pick6()
    console.log('The winning lotto numbers are', winningTicket);
    let matchedNums = matchCheck(playersTicket, winningTicket);
    // console.log(matchedNums, matchedNums.length); 
    console.log('Here are the highly unlikely matches', matchedNums.join(' '));
    for (let i =0; i < matchedNums.length; i++){
        counter += 1
    }
    console.log('this is the amount of matches you got', counter)
    if (counter == 1) {
        moneyBalance += 4
    }
    else if (counter == 2){
        moneyBalance += 7
    }
    else if (counter == 3){
        moneyBalance += 100
    }
    else if (counter == 4){
        moneyBalance += 1000
    }
    else if (counter == 5){
        moneyBalance += 1000000
    }
    else if (counter == 6){
        moneyBalance += 25000000
    }
    else {
        moneyBalance += 0
    }
    let endBalance = money - 2 
    moneyBalance = moneyBalance - endBalance

}
let cost = plays * 2
console.log(moneyBalance)

let returnOnInvestment = (moneyBalance - cost) / moneyBalance
console.log('Your ROI is', returnOnInvestment)