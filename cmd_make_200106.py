game_name = input("The name of the game:")
num_timesteps = input("The num of timesteps:")
gpu_use_index = int(input("The index of the first GPU:"))
total_gpu_num = 3


baseline = prio = dpsr0 = True

# baseline
if baseline:
    print('CUDA_VISIBLE_DEVICES={} '.format(gpu_use_index) +
          'python -m baselines.run --alg=deepq ' +
          '--env={}NoFrameskip-v4 --num_timesteps={} '.format(game_name, num_timesteps) +
          '--save_path=models0113/{}_{}/{}{} '.format(game_name, num_timesteps, 'baseline', '') +
          '--log_path=logs/{}_{}/{}{} '.format(game_name, num_timesteps, 'baseline', '') +
          '--print_freq=1 ' +
          '--dpsr_replay=False ' +
          '--prioritized_replay=False ' +
          '--state_recycle_freq=10000 ' +
          '--dpsr_replay_candidates_size=32')
    gpu_use_index = (gpu_use_index + 1) % total_gpu_num

# prio
if prio:
    print('CUDA_VISIBLE_DEVICES={} '.format(gpu_use_index) +
          'python -m baselines.run --alg=deepq ' +
          '--env={}NoFrameskip-v4 --num_timesteps={} '.format(game_name, num_timesteps) +
          '--save_path=models0113/{}_{}/{}{} '.format(game_name, num_timesteps, 'prio', '') +
          '--log_path=logs/{}_{}/{}{} '.format(game_name, num_timesteps, 'prio', '') +
          '--print_freq=1 ' +
          '--dpsr_replay=False ' +
          '--prioritized_replay=True ' +
          '--state_recycle_freq=10000 ' +
          '--dpsr_replay_candidates_size=32')
    gpu_use_index = (gpu_use_index + 1) % total_gpu_num

# dpsr0
if dpsr0:
    print('CUDA_VISIBLE_DEVICES={} '.format(gpu_use_index) +
          'python -m baselines.run --alg=deepq ' +
          '--env={}NoFrameskip-v4 --num_timesteps={} '.format(game_name, num_timesteps) +
          '--save_path=models0113/{}_{}/{} '.format(game_name, num_timesteps, 'dpsr0') +
          '--log_path=logs/{}_{}/{} '.format(game_name, num_timesteps, 'dpsr0') +
          '--print_freq=1 ' +
          '--dpsr_replay=True ' +
          '--prioritized_replay=False ' +
          '--state_recycle_freq=0 ' +
          '--dpsr_replay_candidates_size=32')
    gpu_use_index = (gpu_use_index + 1) % total_gpu_num

recycle_freq_list = [10000, 20000]
cand_size_list = [8, 16, 32, 64]
state_recycle_max_priority_set_list = [False, True]

for recycle_freq in recycle_freq_list:
    for cand_size in cand_size_list:
        for state_recycle_max_priority_set in state_recycle_max_priority_set_list:
            print(
                # 'conda activate openaivezen; ' +
                'CUDA_VISIBLE_DEVICES={} '.format(gpu_use_index) +
                'python -m baselines.run --alg=deepq ' +
                '--env={}NoFrameskip-v4 --num_timesteps={} '.format(game_name, num_timesteps) +
                '--save_path=models0113/{}_{}/dpsr{}_{}cand_MAX_prio_set_{} '.format(game_name,
                                                                                 num_timesteps,
                                                                                 recycle_freq,
                                                                                 cand_size,
                                                                                 state_recycle_max_priority_set) +
                '--log_path=logs/{}_{}/dpsr{}_{}cand_MAX_prio_set_{} '.format(game_name,
                                                                              num_timesteps,
                                                                              recycle_freq,
                                                                              cand_size,
                                                                              state_recycle_max_priority_set) +
                '--print_freq=1 ' +
                '--dpsr_replay=True ' +
                '--prioritized_replay=False ' +
                '--state_recycle_freq={} '.format(recycle_freq) +
                '--dpsr_replay_candidates_size={} '.format(cand_size) +
                '--dpsr_state_recycle_max_priority_set={}'.format(state_recycle_max_priority_set))
            gpu_use_index = (gpu_use_index + 1) % total_gpu_num
