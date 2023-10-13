# Programming tasks

## Programming task 1

Make use of the template from here: https://colab.research.google.com/drive/1d0sd1TcJaJAqH8cCkdBVpsUoxHW0pyFm?usp=sharing to implement your own version of the algorithm to solve the finite-horizon problem in the frozen lake environment: https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py. <br>
You are expected to take as input the horizon T and the 8x8 arena (i.e., we can change these while evaluating your code) and output the optimal policy on each of the 64 states for that input and the optimal value for state 0 (the top left state). <br>
We will use T < 1000 and to evaluate your solution (cf. the T = 10 in the template for testing reasons). <br>
Stick to the "FrozenLake8x8-v1" environment loaded in the template. <br>
You must submit your solutions as a google colab link (make sure it gives an output in colab before you send it). <br>
Use the instructions provided in the template to run it locally on your computer if you want a visual representation using pygame (optional). <br>
Before submitting, make sure that you have enabled "Anyone on the internet with the link can view" under "Share" and rename your file as "mfrl'23-PT1-your_name.ipynb".

## Programming task 2

Make use of the template from here: https://colab.research.google.com/drive/1d0sd1TcJaJAqH8cCkdBVpsUoxHW0pyFm?usp=sharing to implement your own version of the policy-iteration algorithm to solve the infinite-horizon problem with total expected discounted rewards. We will use \alpha = 0.999 to evaluate your solution.

Make sure to stick to the "FrozenLake8x8-v1" environment loaded in the template.

## Programming task 3

Make use of the template from here: https://colab.research.google.com/drive/1d0sd1TcJaJAqH8cCkdBVpsUoxHW0pyFm?usp=sharing to implement your own version of the value-iteration algorithm to solve the infinite-horizon problem with total expected discounted rewards. We will use \alpha = 0.999 and \epsilon=0.001 to evaluate your solution. <br>
Make sure to stick to the "FrozenLake8x8-v1" environment loaded in the template. <br>
Please keep the following things in mind: <br>

While sharing the colab link, make sure to give access to anyone with the link;
Make sure that your code runs and gives an output before you submit it. The output must have the expected reward of your policy and the random policy for any input
Try to use comments to explain your code wherever it is possible;
You only need to compute the expected reward of vertex 0 (i.e., the vertex in the North-West corner).

## Programming task 4

Make use of the template from here: https://colab.research.google.com/drive/1d0sd1TcJaJAqH8cCkdBVpsUoxHW0pyFm?usp=sharing to implement your own version of the policy-iteration algorithm to solve the infinite-horizon problem with average reward.

As a summary of what is expected of you:

1. You use the policy iteration algorithm to compute an optimal policy for the inifinite-horizon problem with average reward. You need to output your policy for this assignment.

2. You compute the average reward of your policy using Theorem 1.4.7 (item 1).

3. You compute the average reward of a random policy (as given in the template) again using Theorem 1.4.7 (item 1)

4. You print or assert in the code that the average-reward value vector (that is, \phi) of your policy is at least that of the random policy.

If you have questions about this assignment, don't hesitate to contact me (Shrisha) or Guillermo. Also make sure to look at the tips given during the lectures.

## Programming task 5

Make use of the template from here: https://colab.research.google.com/drive/1d0sd1TcJaJAqH8cCkdBVpsUoxHW0pyFm?usp=sharing to implement your own version of Q-learning to solve the infinite-horizon problem with total expected discounted rewards. We will use \alpha = 0.999. Important notes:

(A) Your code to compute the Q-values cannot make use of the prob and rewd dictionaries since that would be cheating. You will need to fix some number of iterations that Q-learning will run for before stopping it, this can be hardcoded and based on some tests performed by you using the steps mentioned below.

(B) Once you stop your Q-learning algorithm you can easily obtain a policy from the Q-values by playing from i an action a which maximizes the value Q(i,a).

(C) To evaluate the policy as obtained above, and compare it to the random policy, you are allowed to use prob and rewd. You are also allowed to recycle your code from previous assignments for this part.

(D) In this case it suffices to compare the (expected dicounted reward) value of your policies from the initial state only.
