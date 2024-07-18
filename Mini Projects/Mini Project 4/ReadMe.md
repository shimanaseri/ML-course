# Mini Project 4 - Learning Objectives

This repository contains solutions to a series of exercises designed to improve understanding of reinforcement learning and artificial intelligence, focusing on classic problems like the Wumpus World and the Lunar Lander.

## What You'll Learn

### Question 1: Solving the Wumpus World

The Wumpus World is a classic AI problem involving a 4x4 grid with a goal of finding gold while avoiding hazards like the Wumpus and pits.

1. **Environment Setup:** Define a 4x4 grid with random positions for gold, Wumpus, and pits. Define the possible actions (move up, down, left, right, and shoot an arrow).

2. **Reward Structure:**
   - +100 for finding gold.
   - -1000 for falling into a pit or being eaten by the Wumpus.
   - +50 for killing the Wumpus.
   - -1 for each move.

3. **Initial Parameters:**
   - Learning rate: 0.1
   - Discount factor: 0.9
   - Exploration rate: Starts at 1.0 and decreases over time.

4. **Tasks:**

   a. **Q-Learning and Deep Q-Learning:** Implement both Q-learning and Deep Q-learning algorithms for the Wumpus World. Train the agent and plot the cumulative rewards over episodes.

   b. **Policy Performance:** Plot the policy performance over episodes for both Q-learning and Deep Q-learning. Compare which algorithm performs better after 1000 episodes.

   c. **Epsilon Impact:** Discuss how different values of epsilon (exploration rate) impact the learning process. What did you observe when epsilon was high versus when it was low?

   d. **Learning Efficiency:** How many episodes did it take for the Q-learning agent to consistently find gold without falling into pits or being eaten by the Wumpus? Compare the learning efficiency of both algorithms.

   e. **Neural Network Architecture:** Describe the neural network architecture used for the Deep Q-learning agent. Why did you choose this architecture?

- <a href="https://github.com/shimanaseri/ML-coarse/blob/main/Mini%20Projects/Mini%20Project%204/q1.ipynb"><strong>Q1 code »</a>

### Question 2: Deep Q-Learning for Lunar Lander

1. **Environment Study:** Examine the Lunar Lander environment. Summarize its state space, action space, and reward system.

2. **Agent Performance:**

   a. **Performance with Different Batch Sizes:** Plot the cumulative rewards per episode for batch sizes of 32, 64, and 128. Record a video of the agent's performance at 50, 100, 150, 200, and 250 episodes.

   b. **Best Performing State:** Choose the best-performing state based on convergence speed to optimal rewards and other criteria. Justify your choice.

   c. **Comparison of DQN and DDQN:** Compare the performance of DQN and DDQN models by plotting cumulative rewards per episode. Record videos of the agent's performance at 100 and 250 episodes for both models.

   d. **Regret Analysis:** Perform a visual analysis of regret for different models and batch sizes.

   e. **Model Checkpoints and Videos:** Save model checkpoints and download them to your system. Record and share videos of the agent’s performance using these models.

## License

This project is licensed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>
