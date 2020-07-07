'''
python -m baselines.run
--alg=deepq
--env=BreakoutNoFrameskip-v4
--num_timesteps=0
--load_path=models/Breakout_1e7/baseline
--play
'''
f = open('test_cmd0113.txt', 'w')

for j in range(5):
    for i in range(19):
        f.write('python -m baselines.run0 sos {} {} && '.format(j, i))
    f.write('\n')
f.close()
