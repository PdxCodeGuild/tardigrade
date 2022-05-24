import requests

response = requests.get("http://hp-api.herokuapp.com/api/characters/students")    
data = response.json() 
# print (f" {data[0]['name']}")

def character(characters):
    dict={}
    for item in range(len(characters)):
        word= characters[item]
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


x= character(data)

# def questions():
#     hair=input ('choose a hair color')
#     pass


