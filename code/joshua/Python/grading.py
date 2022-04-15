
def grade():
    user_score = int(input('What is your score?\n'))
    scored_letter = ['A','B','C','D','F']

    if user_score >= 90 or user_score >= 100:
        print(f'Your letter grade is: {scored_letter[0]}')
        
    
    elif user_score >= 80 or user_score >= 89:
        print(f'Your letter grade is: {scored_letter[1]}')
        
   
    elif user_score >= 70 or user_score >= 79:
        print(f'Your letter grade is: {scored_letter[2]}')
        
   
    elif user_score >= 60 or user_score >= 69:
        print(f'Your letter grade is: {scored_letter[3]}')
        
  
    elif user_score >= 0 or user_score >= 59:
        print(f'Your letter grade is: {scored_letter[4]}')
        
    else:
        print('Not a valid input')

grade()