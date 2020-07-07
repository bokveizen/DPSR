import csv
import numpy as np

game_name = input('game_name:')
model_timesteps = input('model_timesteps:')
with open('res200113/res_{}_{}.txt'.format(game_name, model_timesteps)) as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
    for row in csv_reader:
        data.append(row)
data_len_per_method = 300 + 1
method_num = len(data) // data_len_per_method
res = []
for i in range(method_num):
    method_test_res = [float(data[j][0]) for j in range(data_len_per_method * i + 1, data_len_per_method * (i + 1))]
    method_average_rew = np.average(method_test_res)
    method_best_rew = np.max(method_test_res)
    res.append([data[data_len_per_method * i], method_average_rew, method_best_rew])
res.sort(key=lambda x: x[1], reverse=True)
for i in res:
    print(i)
