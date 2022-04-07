from re import X


def loud_text(text):
    word = ("-").join(list(text)).upper()
    return word


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



def double_letters(word):
    double = ''
    for letter in word:
        double += letter*2
    return double


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'





def count_letter(letter, word):
    x = 0

    for item in word:
        if item == letter:
            x += 1
    return x


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2







# def latest_letter(word):
    


# def test_latest_letter():
#     return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'





# def count_hi(text):
#     for 


# def test_count_hi():
#     assert count_hi('hihi') == 2
#     assert count_hi('hello hi llama hill') == 2







def snake_case(text):
    word = str(text).lower().replace(' ', '_')
    for item in word:
        # if item in '`,~,!,@,#,$,%,^,&,*,(,),-,+,=,{,[,},},|,:,;,",,<,,,>,.,?':
        #     word.remove(item,'')   figure out how to replace special characters
        
    return word
        


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'