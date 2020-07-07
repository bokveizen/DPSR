import gym
import copy
import numpy as np

# env = gym.make('Pong-ramNoFrameskip-v4')
env = gym.make('KrullNoFrameskip-v4')
env.reset()

env_clone_state0 = env.clone_state()
obs_at_clone = None
for _ in range(10):
    obs_at_clone, *_ = env.step(env.action_space.sample())
env_clone_state = env.clone_state()
obs, *_ = env.step(0)

env1 = copy.deepcopy(env)
env1.restore_state(env_clone_state)
obs1, *_ = env1.step(0)

env2 = gym.make('Pong-ramNoFrameskip-v4')
env2.reset()
env2.restore_state(env_clone_state)
obs2, *_ = env2.step(0)

env3 = gym.make('Pong-ramNoFrameskip-v4')
env3.reset()
env3.restore_state(env_clone_state)
obs3, *_ = env3.step(0)

print(np.sum(obs == obs1))
print(np.sum(obs == obs2))
print(np.sum(obs == obs3))
env.close()
