function pick6() {
    let pickList = [];
    for (let i = 0; i < 6; i++) {
        pickList.push(Math.floor(Math.random() * 100));
    }
    return pickList
}

function tix6() {
    let pickList = [];
    for (let i = 0; i < 6; i++) {
        pickList.push(Math.floor(Math.random() * 100));
    }
    return pickList
}

function match_list(x, y) {
    let matched_list = [];
    for (let i = 0; i < x.length; i++) {
        for (let j = 0; j < y.length; j++) {
            if (x[i] === y[j])
                matched_list.push(x[i]);
        }
    }
    return matched_list
}

function game() {

    let balance = 0;
    let expenses = 0;
    let number = 0;
    let totalGames = 100000;


    while (number <= totalGames) {
        let picks = pick6();
        let winningNum = tix6();
        expenses += 2;
        let winner = match_list(picks, winningNum);
        let count = winner.length;
        if (count == 1) {
            balance += 4;
        } else if (count == 2) {
            balance += 7;
        } else if (count == 3) {
            balance += 100;
        } else if (count == 4) {
            balance += 50000;
        } else if (count == 5) {
            balance += 1000000;
        } else if (count == 6) {
            balance += 25000000;
        } else {
            balance += 0
        }
        number++;
    }

    console.log('Total Balance:', balance);
    console.log('Total Expenses:', expenses);
    console.log('ROI:', (balance - expenses) / expenses);
}

game()