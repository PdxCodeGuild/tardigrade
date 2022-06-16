// -----------------------------------------------------------------
// Random Number Generator
console.log("----------------TESTING-------------------")

function getRandomNumber() {
    min = Math.floor(1)
    max = Math.ceil(99)
    randomNum = Math.floor(Math.random() * (max - min + 1) + min);
}

// -----------------------------------------------------------------
// Winning Number(s) Generator

let winningNumbers = []

function winningNumbersGenerator() {
    for (let i = 0; i < 6; i++) {
        getRandomNumber();
        winningNumbers.push(randomNum);
    }
}

    // winningNumbersGenerator()
    // console.log('TS Winning Numbers List: ', winningNumbers) // TEST STATEMENT

    // -----------------------------------------------------------------
    //  Ticket Number(s) Generator

    function ticketNumbersGenerator() {
        ticketNumbers = [];
        for (let j = 0; j < 6; j++) {
            getRandomNumber();
            ticketNumbers.push(randomNum);
        }
    }

    // ticketNumbersGenerator()
    // console.log("TS Your Ticket Numbers: ", ticketNumbers) // TEST STATEMENT

    // -----------------------------------------------------------------

    function numMatches() {
        matches = 0
        for (let k = 0; k < 6; k++) {
            if (winningNumbers[k] == ticketNumbers[k]) {
                matches++
            }
        }
    }

    // numMatches()
    // console.log("TS Number of Matches: ", matches) // TEST STATEMENT

    // -----------------------------------------------------------------
    // Winnings Calculcator

    balance = 0

    function winningsCalculator() {
        balance += -2
        if (matches == 1) {
            balance += + 4
        }
        else if (matches == 2) {
            balance += 7
        }
        else if (matches == 3) {
            balance += 100
        }
        else if (matches == 4) {
            balance += 50000
        }
        else if (matches == 5) {
            balance += 1000000
        }
        else if (matches == 6) {
            balance += 25000000
        }

    }
    // winningsCalculator()
    // console.log("Final Balance: $", balance)


    // -----------------------------------------------------------------

    console.log("---------------MAIN GAME------------------")
    // -----------------------------------------------------------------

    function pick6() {

        winningNumbersGenerator();
        console.log('TS Winning Numbers List: ', winningNumbers); // TEST STATEMENT
        
        // Invoke loop
        for (i = 0; i < 100000; i++) {
            ticketNumbersGenerator();
            console.log("TS Your Ticket Numbers: ", ticketNumbers) // TEST STATEMENT
            numMatches();
            console.log("TS Number of Matches: ", matches); // TEST STATEMENT
            winningsCalculator();
            console.log("Final Balance: $", balance); // TEST STATEMENT
        }
    }

pick6()