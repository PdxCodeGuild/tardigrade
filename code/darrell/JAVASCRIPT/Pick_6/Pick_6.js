
const winning = [];

function pick6() {

    for (let i = 0; i < 6; i++){
        randomNum = Math.floor(Math.random() * 100);
        winning.push(randomNum)
    }    
    console.log(winning)
    return winning
}

function numMatches() {
    let balance = 0
    let expenses = 0
    let earnings = 0
    let ticket = [];

    for (let i = 0; i < 1000; i++){
        
        for (let j = 0; j < 6; j++){
            randomNum = Math.floor(Math.random() * 100);
            ticket.push(randomNum);
        }     
    } 
    console.log(ticket);   
 
    console.log(`Ticket: ${ticket}`);
        balance -= 2;
        expenses -= 2;
        let matches = [];
        for (let i = 0; i < ticket.length; i++) {
            if (ticket[i] == winning[i]){
                matches.push(ticket[i]);
                console.log(`Matches: ${matches}`);
            }    if (matches.length == 1) {
                    balance += 4;
                    earnings += 4;
            }   else if (matches.length == 2) {
                    balance += 7;
                    earnings += 7;
            }   else if  (matches.length == 3) {
                    balance += 100;
                    earnings += 100;
            }   else if  (matches.length == 4) {
                    balance += 50000;
                    earnings += 50000;
            }   else if  (matches.length == 5) {
                    balance += 1000000;
                    earnings += 1000000;
            }   else if  (matches.length == 6) {
                    balance += 25000000;
                   earnings += 25000000;
            } 
        
        }  
        
    let ROI = earnings - expenses/expenses;
    ROI *= 100;
    console.log(`Your current balance: ${balance}`);
    console.log(`Your earnings: ${earnings}`);
    console.log(`Your expenses: ${expenses}`);
    console.log(`Your ROI: ${ROI}%`);
    
}

pick6()
numMatches()





