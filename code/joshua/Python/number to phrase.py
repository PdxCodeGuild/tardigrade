

def user_phrases(user):
    phrases = {
    0:'zero', 
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eighty',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'one hundred',
    200:'two hundred',
    300:'three hundred',
    400:'four hundred',
    500:'five hundred',
    600:'six hundred',
    700:'seven hundred',
    800:'eighty hundred',
    900:'nine hundred',
    }
    for key in phrases.keys():
        if key == user:
            print(phrases[key])
            break
        elif len(str(user)) == 2 and  user not in phrases:
            numba = []
            for i in str(user):
                numba.append(i)
            fir = int(numba[0] + '0')
            sec = int(numba[1])
            print(phrases[fir] + '-' + phrases[sec])
            break
        
        
        
        elif len(str(user)) == 3 and  user not in phrases:
            numba = []
            for i in str(user):
                numba.append(i)
            fir = phrases[int(numba[0])] + ' hundred'
            if numba[1] == '0':
               sec = ' and '
            else:
                sec = (' and ' + phrases[int(numba[1]+'0')] + ' ')
            # sec = int(numba[1] + '0')
            thi = phrases[int(numba[2])]
            print(fir + sec + thi)
            break

            








for i in range(100, 999):   
    x = i
    user_phrases(x)



            