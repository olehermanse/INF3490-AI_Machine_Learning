# Reinforcement Learning (RL)

## Example - Chess AI
 * Not a simple classifier, cannot calculate *error*
 * Outcome after ~40 turns
    * Win or lose
    * Very limited information
 * Reward based on action
    * Taking a piece, attacking or defending can have rewards
    * Optimize short term and long term rewards

## Reward function
* Similar to fitness function
* Negative reward is possible - punishment
* Can be given based on action(throughout the episode) or outcome (in the end).
* Maximize total Reward

## Value
* The value of an action is the reward we expect that action to give
* Two ways to look at:
    * V(s) = Value of state
    * Q(s,a) = Value of state + action

### Q-Learning
* Update Q values with a learning rate (similar to MLP!)
* Off-policy

### SARSA
* On-policy
* Will randomly make some mistakes
* Results in safer behavior
