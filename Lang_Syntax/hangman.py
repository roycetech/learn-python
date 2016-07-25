def get_valid_letter():    
    while True:
        letter = input('Please enter a letter: ')
        if letter.isdigit() == True:
            print('That is a number!')
        elif len(str(letter)) >1:
            print("Sorry, you have to enter exactly ONE letter")
        else:
            return letter

get_valid_letter()