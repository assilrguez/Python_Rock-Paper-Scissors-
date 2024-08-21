import time
import random

class Player:
    """Making newPlayer as object"""
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.pick = None

def is_winner(player,bot):
    """Determine the winner and update the score."""
    win_conditions = {
        'R': 'S',
        'P': 'R',
        'S': 'P'
    }
    if player.pick == bot.pick:
        result = "It's a DRAW!"
    elif win_conditions[player.pick] == bot.pick:
        player.score += 1
        result = f"{player.name} is the winner!"
    else:
        bot.score += 1
        result = f"{bot.name} is the winner!"
    print(result)

def play_round(player,bot):
    """Play a round or quit"""
    player.pick = input("Pick (R)ock, (P)aper, or (S)cissors: ").upper().strip()
    if player.pick not in ('P','R','S',"QUIT"):
        print("Please pick P or R or S")
        return True
    if player.pick == "QUIT":
        return False
    bot.pick = random.choice(('P','R','S'))
    print(f"You pick {picks[player.pick]}\nComputer pick {picks[bot.pick]}")
    is_winner(player,bot)
    print(f"{player.name}:{player.score} VS {bot.name}:{bot.score}")
    return True

picks = {'R':"Rock",'P':"Paper",'S':"Scissors"}      
name = input("Enter name : ")
player = Player(name)
bot = Player("computer")
time.sleep(1)
print(f"Hello {name}, Welcome to Rock Paper Scissors")
time.sleep(1)
print("select a game mode by puting the number :")
time.sleep(1)
print("1) Infinite\n2) Play to a set score")
time.sleep(1)
try:
    game_mode = int(input("->"))
    if (game_mode not in (1,2)):
        raise ValueError("Sorry something went wrong!\nPlease choose either 1 or 2 .")
    else:
        if game_mode == 1:
            print("If you want to quit write \"quit\"")
            while(play_round(player,bot)):
                pass
        else:
            try:
                target_score = int(input("Enter the target score: "))
                if target_score <= 0:
                    raise ValueError
                while((bot.score<target_score) and (player.score<target_score)):
                    play_round(player,bot)
            except ValueError:
                print("Invalid input !,\nEnter a valid score")
except ValueError:
    print("Invalid input. Please choose either 1 or 2.")