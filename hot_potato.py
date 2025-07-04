import random
print('Welcome to the hot potato game')
print('The rules of the game are as the following: There is a hot potato and there are n passes and whoever ends up with the potato at the end is eliminated\nThe last one standing wins.  ')
players=[]
nplayers=int(input('How many players are in the game?'))
for i in range(nplayers):
    name=input('Enter the player name:')
    players.append(name)
passes=random.randint(1,10)
print('We are passing the potato ', passes, ' times')
while len(players)>1:
    for i in range(0,passes):
        x=players.pop(0)
        players.append(x)
    eliminated=players.pop(0)
print('The winner is',players.pop(0))