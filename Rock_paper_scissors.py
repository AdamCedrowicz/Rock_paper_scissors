#library
import random as r
#game
possible_input = ['p','r','s']

def game():
    opponent = r.choice(possible_input)
    user = input("'p' - paper, 'r' - rock, 's' - scissors."\
        " What's your choice?"\
            " ")  
       
    while user.lower() not in possible_input:
        user = input("Incorrect input, you need choose 'p', 'r' or 's'. Fill it once again please. ")
    else:
        pass
    
    user = user.lower()  
    print(user)
    print(opponent)
    if user == opponent:
       return " It's a draw"

    if you_won (user,opponent):
      return 'You won!'

    return 'Opponent won!'
### condition
def you_won (user,opponent):
    if (user == 'p' and opponent == 'r') or (user == 'r' and opponent == 's') or \
       (user == 's' and opponent == 'p'):
       return True
print(game())