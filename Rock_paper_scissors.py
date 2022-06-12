#library
import random as r
#game
def game():
    opponent = r.choice(['p','r','s'])
    user = input("'p' - paper, 'r' - rock, 's' - scissors."\
        " What's your choice?"\
            " ")     

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
