# new_dictionary = {'apple': 'lime', 'banana': 'yellow'}
# new_dictionary['apple'] += 'green'
# print(new_dictionary)

# print('keys', new_dictionary.keys())
# print('values', new_dictionary.values())
# print('items', new_dictionary.items())

# for key, value in new_dictionary.items():
#     print('key', key)
#     print('value', value)

# for element in new_dictionary:
#     print(element, new_dictionary[element])

## Socks Exercise
pair_socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]

drawer = { 
}

for sock in range(len(pair_socks)):
    single_sock = pair_socks[sock]
    if single_sock in drawer:
        drawer[single_sock]+=1
    else:
        drawer[single_sock]=1

pair = 0

for key, value in drawer.items():
    pair+= value//2

print(drawer)
print(pair)