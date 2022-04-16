import random 
balance = 0
winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
def compare(ticket, win_num):
        match_count = 0
        for i in range(0, len(ticket)-1):
            if ticket[i] == win_num[i]:
                match_count += 1
            else:
                pass
            return match_count

def generate_numbers(size):
    ticket = random.sample(range(1, 99), size)
    win_num = random.sample(range(1, 99), size)
    return (ticket, win_num)

for x in range(100000):
    balance -= 2
    x = compare(*generate_numbers(6))
    balance += winnings[x]
expenses = 200000
roi = (balance/expenses)*100
earnings = balance + expenses
print(f'Your net winnings are ${balance}.\nEarnings: ${earnings}\nExpenses: $200,000\nROI: {roi}')
    