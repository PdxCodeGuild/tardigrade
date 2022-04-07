import string
tc1 = 'Hello World!'
tc2 = 'This is another example.'
def snake_case(con):
    text = con.replace(' ','_')
    text_1 =text.replace('!','')
    return text_1.lower()

print(snake_case(tc1))


import string
tc1 = 'Hello World!'
tc2 = 'This is another example.'
def snake_case(con):
    text = con.replace(' ','_')
    text_1 =text.replace('.','')
    return text_1.lower()

print(snake_case(tc2))