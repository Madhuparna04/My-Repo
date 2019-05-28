This Folder contains code for Q-learning algorithm.

1. Tabular Q-learning - The file <mark>ql.py</mark> contains code for tabular Q-learning used on a 3X3 grid. This [blog](https://marl-ieee-nitk.github.io/reinforcement-learning/2018/12/11/Q-learning.html) explains the algorithm, the 3X3 grid and effects of hyperparameters.

2. Deep Q-Network - DQN uses Neural Networks to find the Q-values corresponding to different actions given the current state. It uses the method of stacking states i.e. the input given to the Neural Network is not one state but say 4 states stacked together. The code uses Cartpole Environment from OpenAI Gym. to test the DQN algorithms.

3. Deep Recurrent Q-Network - DRQN uses lstm along with fully connected layers to approximate Q-values given a state. The input to the network is just one single state and no stacking states is required as lstm can learn dependencies between states. This [blog](https://marl-ieee-nitk.github.io/deep-reinforcement-learning/2019/01/06/DRQN.html) explains the DRQN algorithm and code.

4. Little Mario Game - It is a simplified version of Super Mario. It is a simple game in which the agent needs to learn to jump whenever there is an obstacle. The code uses tabular Q-learning to solve the game.