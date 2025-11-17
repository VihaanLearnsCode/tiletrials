#pit different agents against each other
from tests.naivemaxtile import agent_maxboard
from tests.naivesolve import agent_maxtile
from tilegame.create import *
import time

genboard = generate().copy()
n = 1000

print("Board Generated!")

agent1_name = "Maxboard"
agent2_name = "Maxtile"

best_sequence_1,  tile_nums_1 = agent_maxboard(genboard.copy(), n)[3:]
print(f"Agent {agent1_name} finished playing")

best_sequence_2,  tile_nums_2 = agent_maxtile(genboard.copy(), n)[3:]
print(f"Agent {agent2_name} finished playing")

print(" ")
print("...")
print(" ")

time.sleep(3)

len1 = len(best_sequence_1)
len2 = len(best_sequence_2)

score_1 = sum(1 for t1, t2 in zip(tile_nums_1, tile_nums_2) if t1 > t2)
score_2 = sum(1 for t1, t2 in zip(tile_nums_1, tile_nums_2) if t2 > t1)

diff = abs(score_1 - score_2)

if score_1 > score_2:
    flag = True
elif score_1 < score_2:
    flag = False
else:
    if len1 > len2:
        flag = True
    elif len1 < len2:
        flag = False
    else:
        print(f"It is a tie!")

if flag:
    print(f"Agent {agent1_name} wins by {diff} points!")
else:
    print(f"Agent {agent2_name} wins by {diff} points!")



