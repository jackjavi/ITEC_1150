from pathlib import Path
import os

print('Using the pathlib module and the Path function')
print("Results of running: Path('users', 'shared', 'android')")
path = Path('users', 'shared', 'android')
print(path)

print('Results of running: os.getcwd()')
curr_dir = os.getcwd()
print(curr_dir)

base_dir = os.getcwd()
print('Initital working directory: {}'.format(base_dir))
os.chdir(r'..')
print('One directory up: {}'.format(os.getcwd()))
os.chdir(base_dir)
print('Back to initial working directory: {}'.format(os.getcwd()))