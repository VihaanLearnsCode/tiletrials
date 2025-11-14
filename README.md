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

The parts below this detail how I used the completed simulator.

# Testing Methods and Logical Guessing
I ran 10000 randomly generated games for each guessed sequence. For the sequence, I allowed upto 2000 repeats, as I noticed the average number of moves to complete a game were usually below 1000. Hence, even though I allow for an upper bound of 20 million moves, I am running 2-6 million moves due to most games hitting "Game Over" early.

Putting a limit on the sequence also adds complexity to each guess. For example, if my sequence is "SD", to snake-weight towards the bottom-right corner, and I then try "ASD", to move left every so often, to avoid stuck boards, then I should also notice that A will be performed at the same rate as S or D, as in, 33% of the time, which is not snake-weighting anymore.

With the 10 character limit, I have the space to have A only perform 10% of the time ("ASDSDSDSDS"), which is closer to what I want, but still contains an A to shake things up and maybe save a stuck board from a game over and wasting moves. 

At one point, I thought of adding logic to help a game get unstuck. In fact, I did. For example, if a game is not over, but the sequence does not contain/ is not at a viable move, then it would play a random one. However, that defeats the purpose of the experiment of building a sequence that I think can beat the game, so I removed it.

# Results
Here are the plotted results for 10000 games for the pattern "ASDS":

![Results](images/Distribution_ASDS.png)

Time taken = 4 minutes 57 seconds

Average number of moves = 311

Best Tile / Frequency    

32  : 9

64  : 193

128 : 1698

256 : 5277

512 : 2799

1024 : 24       

Almost there!! The aim to would be to push the dark plotted band further up, so that we get closer to 2048.

I will update more findings here and, if it is done, on my personal [website](https://vihaanlearnscode.github.io/).

# Acknowledgements:
This project, by its nature, draws heavy inspiration from Gabriele Cirulli, the creator of the popular [2048](https://github.com/gabrielecirulli/2048).
However, in the spirit of learning from this endeavor, I never looked at the linked code myself, and so my implementation will differ.

