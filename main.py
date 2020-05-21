import gym
import random
import itertools
import matplotlib
import numpy as np
import pandas as pd
import sys
import pickle


LEARNING_RATE = 1.0
MINIMUM_LEARNING_RATE = 0.003
MAX_EPISODES = 10000
MAX_STEPS_PER_EPISODE = 10000
NUMBER_OF_STATES = 20
EPSILON = 0.02



#ENUM
CART_POSITION = 0
CART_VELOCITY = 1
POLE_ANGLE = 2
POLE_VELOCITY = 3


env = gym.make('CartPole-v0')
env.reset()
policy_table = np.zeros((NUMBER_OF_STATES,NUMBER_OF_STATES, env.action_space.n))


#-----------------------------------------------------------------------------------

def bellman(**kwargs):
    reward = kwargs.get('reward')
    learning_rate = kwargs.get('learning_rate')
    discount_rate = kwargs.get('discount_rate')
    present = kwargs.get('present')
    future = kwargs.get('future')
    return present + learning_rate * (reward + discount_rate * np.max(future) - present)

def decreasedLearningOverTime(episode):
    return max(MINIMUM_LEARNING_RATE, LEARNING_RATE * (0.85 ** (episode//100)))

def getObservations(env, obs):
    env_low = env.observation_space.low
    env_high = env.observation_space.high
    env_dx = (env_high - env_low) / NUMBER_OF_STATES
    values = []
    print(env.action_space.n)
    for i in range(env.observation_space.shape[0]):
        values.append( int((obs[i] - env_low[i])/env_dx[i]) )
    return tuple(values)

def getState(env, obs):
    state = policy_table
    for value in getObservations(env, obs):
        state = state[value]
    return state
#-----------------------------------------------------------------------------------


# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample()) # take a random action
# env.close()

def findSolution(episodes, steps):
    for episode in range(MAX_EPISODES):
        obs = env.reset()
        score = 0
        learning_rate = decreasedLearningOverTime(episode)
        for _ in range(MAX_STEPS_PER_EPISODE):
            a, b, c, d, getObservations(env, obs)
            env.render()
            if np.random.uniform(0, 1) < EPSILON:
                action = np.random.choice(env.action_space.n)
            else:
                logits = policy_table[a][b]
                logits_exp = np.exp(logits)
                probs = logits_exp / np.sum(logits_exp)
                action = np.random.choice(env.action_space.n, p=probs)
            obs, reward, done, _ = env.step(action)
            if done:
                break
            
        # for _ in range(MAX_STEPS_PER_EPISODE)
findSolution(10, 10)