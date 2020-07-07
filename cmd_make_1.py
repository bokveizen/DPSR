'''
python -m baselines.run
--alg=deepq
--env=BreakoutNoFrameskip-v4
--num_timesteps=0
--load_path=models/Breakout_1e7/baseline
--play
'''
import os
game_name = 'Tennis'
model_timesteps = '1e6'
methods = os.listdir('models/{}_{}'.format(game_name, model_timesteps))
f = open('test_cmd_{}_{}.txt'.format(game_name, model_timesteps), 'w')
# for method in methods:
#     f.write('python -m baselines.run ' +
#             '--alg=deepq ' +
#             '--env=KungFuMasterNoFrameskip-v4 ' +
#             '--num_timesteps=0 ' +
#             '--load_path=models/KungFuMaster_1e6/' + method + ' ' +
#             '--play & ')
for i in range(len(methods)):
    f.write('python -m baselines.run2 sos ' + str(i) + '&')
f.close()
