import random
from queues import queue_actions
print('Welcome to the hot potato game')
print('The rules of the game are as the following: There is a hot potato and there are n passes and whoever ends up with the potato at the end is eliminated\nThe last one standing wins.  ')
#players=[]
players=queue_actions()
nplayers=int(input('How many players are in the game?'))
for i in range(nplayers):
    name=input('Enter the player name:')
    players.enqueue(name)
passes=random.randint(1,10)
print('We are passing the potato ', passes, ' times')
while players.size()>1:
    for i in range(0,passes):
        x=players.dequeue()
        players.enqueue(x)
    eliminated=players.dequeue()
print('The winner is',players.dequeue())