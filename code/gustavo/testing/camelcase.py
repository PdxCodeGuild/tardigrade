import string


tc1 = 'Hello World!'
tc2 = 'This is another example.'

def camel_case(con):
    text = con.split()
    text_ls = list(text)
    text_ls = text_ls[0].lower() + text_ls[1].title()
    text_ls = str(text_ls).replace('!','')
    return text_ls


print(camel_case(tc1))

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

tc1 = 'Hello World!'
tc2 = 'This is another example.'

def camel_case(con):
    text = con.split()
    text_ls = list(text)
    text_ls = text_ls[0].lower() + text_ls[1].title() + text_ls[2].title() + text_ls[3].title()
    text_ls = str(text_ls).replace('.','')
    return text_ls


print(camel_case(tc2))