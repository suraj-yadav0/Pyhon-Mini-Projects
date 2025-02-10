import random

def play_game():
    choices = ['stone','paper','scissor']
    
    rules = {
        'stone': 'scissor',
        'paper': 'stone',
        'scissor': 'paper'
    }
    
    
    while True:
        computer =  random.choice(choices)
        player = input('Enter stone , rock or paper : (or q to quit) :').lower()
        
        
        if player == 'q':
            print('Thanks for playing')
            break
        
        if player not in choices:
            print('Invalid choice')
            continue
        
        print('You chose :' + player)
        
        print('Computer chose :' + computer)
        
        
        if player == computer:
            print('Its a tie')
        elif rules[player] == computer:
            print('You win')
        else:
            print('You lose')
            
            
play_game()
        
        
        
        