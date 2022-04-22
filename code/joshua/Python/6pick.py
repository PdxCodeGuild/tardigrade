from cmath import pi
import random
from turtle import pos

def wintik():
    pick = []
    for i in range(6):
        pick.append(random.randint(1,99))
    # pick = [1,1,1,3,1,0]
    return pick

def comptik():
    pick = []
    for i in range(6):
        pick.append(random.randint(1,99))
    # pick = [0,0,0,0,0,0]
    return pick


def com_balan(winners):
    cur_bal = 0
    if winners == 1:
        cur_bal += 4

    elif winners == 2:
        cur_bal += 7

    elif winners == 3:
        cur_bal += 100

    elif winners == 4:
        cur_bal += 50000

    elif winners == 5:
        cur_bal += 1000000

    elif winners == 6:
        cur_bal += 25000000

    else:
        cur_bal = 0

    return cur_bal

def counter(win,data):

    for key in data.keys():
        if key == win:
            data[key] += 1
    return data


wintick = wintik()
comptick = comptik()




def pick6(wintik):
    balance = 0
    chances = 100000
    data = {0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
            }
    for j in range(chances):
        balance -= 2
        winners = 0
        for i in range(6):
            comptik()
            if wintik[i] == comptick[i]:
                winners += 1
        balance += com_balan(winners)
        data = counter(winners,data)



    print(f"""
    The computers final balance after {chances} tries is ${balance + 2}.
    Stats for the computer goes as follows:
    {str(data).replace('{','').replace('}','')}
     """)


pick6(wintick)