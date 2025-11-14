# tiletrials
A 2048 tile game WASD simulator. 
This project will generate a 4x4 NumPy representation of the 2048 game, to be used in simulations to find a simple way to win.

# Motivation

The strongest motivation for this project is to find an easy way for me to win 2048.
There are already well documented strategies to get a good score in the game 2048, such as expectiminimax or snake-weighting towards a corner. However, I want to see if there was a short, repeatable, easily memorable pattern of ( <= ~10) moves that could acheive at least one '2048' tile a good chunk of the time on random boards. An example could be ASDSW, where W,A,S,D commonly represent the 4 directions in video gaming. 

There probably exist robust mathematical or algorithmic approaches to proving/finding such a strategy (eg. [MDP approach](https://jdlm.info/articles/2018/03/18/markov-decision-process-2048.html)). Given the results from that link and the stochastic nature of the game, I personally hypothesize that I will not find such a pattern, especially given my self-imposed constraint of ~10 moves. In fact, if such a pattern existed, I'm sure that would've been a well-known fact by now. However, the journey (building the game myself and seeing how far my guesses can get) to proving that right (or, hopefully, wrong) for myself is my real reward. 

# Outline
  1) I will first attempt to accurately build my own version of 2048
  2) Then, I plan to simulate a variety of self-selected patterns on generated boards to see how they perform
  3) Finally, I'll collect some (hopefully) thought-provoking statistics based on the results

# Goals
  1) To find a viable short sequence of moves that can comfortably score a 2048 tile
  2) To overcome any math/coding-related subproblems I come across while using clean coding practices
  3) To try my hand at small-scale, informal independent research (define, hypothesize, test, collect)

Finally, I enjoy casual coding and the process of building things, so I hope to have a lot of fun!

# Results
Here are the results for 10000 games for the pattern "ASDS":

Time taken = 4 minutes 57 seconds
Average number of moves = 311

Best Tile / Frequency    

32               9

64               193

128              1698

256              5277

512              2799

1024             24       


Almost there!!


I will update my more findings here and, if it is done, on my personal [website](https://vihaanlearnscode.github.io/).

# Acknowledgements:
This project, by its nature, draws heavy inspiration from Gabriele Cirulli, the creator of the popular [2048](https://github.com/gabrielecirulli/2048).
However, in the spirit of learning from this endeavor, I never looked at the linked code myself, and so my implementation will differ.

