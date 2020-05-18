import gym
import agents

# print(agents.get('Test'))

env = gym.make('CartPole-v0')
num_of_episodes = 5
num_of_steps = 1000
sum_reward_running = 0
agent = agents.get('Test', env)

for episode in range(num_of_episodes):
    state = env.reset()

    sum_reward = 0
    laststep = None
    for step in range(num_of_steps):
        # print(obs)
        action = agent.get_action(state)
        (obs, reward, done, _) = env.step(action)
        print(obs)
        sum_reward += reward
        env.render()
        if done:
            print("Episode %s done after %s steps" % (episode, step + 1))
            break

    sum_reward_running = sum_reward_running * 0.95 + sum_reward * 0.05
    print('%d running reward: %f' % (episode, sum_reward_running))


env.close()