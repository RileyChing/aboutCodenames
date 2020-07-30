import gym
from matplotlib import pyplot
from collections import defaultdict

env =

env.actionspace_space, env.observation_space


def sample_policy(observation):
    return 0




def generate_episode(policy, env):
    states, actions, rewards = [], [], []
    observation = env.reset()
    while 1:
        states.append(observation)
        action = policy(observation)
        actions.append(action)
        observation, reward, done, info = env.step(action)
        rewards.append(reward)

        if done:
            break

    return states, actions, rewards

def get_value_table(policy, env, n_episodes):
    value_table  = defaultdict(float)
    N = defaultdict(int)

    for _ in range(n_episodes):
        states, _, rewards = generate_episode(policy, env)
        returns = 0

def polt_codenames(V, ax1, ax2):
    