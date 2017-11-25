"""
    Good general-purpose agents don't need to know the semantics of the observations:
    they can learn how to map observations to actions to maximize reward without any
    prior knowledge.
    That said, it's:
    [position of cart, velocity of cart, angle of pole, rotation rate of pole].

    Defined at https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py#L75

    The reward is measured by the number of steps before the pole becomes more than 15
    degrees away from the vertical position. The longer you remain within this range,
    the bigger your total reward is.

    The only way to control the pendulum is by choosing a horizontal direction for the cart to
    move (either to left or right).
"""
import gym

env = gym.make('CartPole-v0')
obs = env.reset()



for step_idx in range(50):
    env.render()
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
    print(obs, reward, done, action)
