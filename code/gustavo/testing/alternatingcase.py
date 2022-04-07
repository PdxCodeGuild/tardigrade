# Alternating Case
# Write a function that converts text to alternating case.
tc1 = 'Hello World!'
tc2 = 'This is another example.'

def alternating_case(con):
    text = con[0:-1:2]
    print(text)





print(alternating_case(tc1))

def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'










# string[start_index : end_index : increment].


