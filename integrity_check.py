import os

TIMESTEPS = '1e6'
while True:
    a = input('Input the date:')
    b = input('Input the alpha 2:')
    c = input('Input the CRC number:')
    if a == 'quit' or b == 'quit' or c == 'quit':
        exit(0)
    model_path = 'models{}_{}_{}_{}'.format(a, TIMESTEPS, b, c)
    if os.path.exists(model_path):
        d = [len(os.listdir(os.path.join(model_path, i))) for i in os.listdir(model_path)]
        print(len(d), d)
    else:
        print('ERROR: NO SUCH PATH.')
