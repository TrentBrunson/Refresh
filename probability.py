#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
results = []
num_game = 10000     # number of games, in each game, we start a new game with one white ball and one black ball, and run the game until the trail number below is reached
all_game_result = []
trial = 100
for j in range(num_game):
    bin = ['B', 'W']
    for i in range(trial):
        bin_size = len(bin)
        choice = np.random.randint(1, bin_size+1)
        if bin[choice-1] == 'B':
            bin.append('B')
        else:
            bin.append('W')
        n = len(bin) - 1
        # print(bin)
        # print('Count of W = ', bin.count('W'))
        # print('N - 1 = ', n)
        if 1 <= bin.count('W') <= n:
            # print('Pass')
            results.append('Pass')
        else:
            print('Fail')
            results.append('Fail')
        # print()
    # print('----------- Outcome-------------------------')
    # print('# of Fails = ', results.count('Fail'))
    # print('# of Pass = ', results.count('Pass'))
    # print('Count of W at the end of one random game = ', bin.count('W'), '\t\t Total # of balls = ', len(bin))
    all_game_result.append(bin.count('W'))
#%%
count = []      # count the number of games that has certain number of white balls at the end of that game
probability = []
number_white_balls = []
for i in range(1, (trial+2)):           # for example, if trial is 100, then the total # of all balls at the end should be 102, the range of possible white ball is from 1 to 101
    count.append(all_game_result.count(i))
    probability.append(count[-1]/num_game)
    number_white_balls.append(i)
#%%
plt.scatter(number_white_balls, probability)
plt.xlabel("Number of possible white balls")
plt.ylabel("Probability")
plt.ylim(-0.002, 0.05)
plt.show()
# %%
