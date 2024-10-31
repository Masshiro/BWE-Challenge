import os
import json
import random
from pathlib import Path
import json
import numpy as np


def load_file_paths(data_dir, chunk_num):
    file_paths = []
    chunk_idx = [f'chunk_{i}' for i in range(chunk_num)]
    for chunk in chunk_idx:
        chunk_path = Path(data_dir) / chunk
        for file in chunk_path.glob("*.json"):
            file_paths.append(file)
    return sorted(file_paths)

def play_with_one_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    print('*'*20)
    print('json structure:\n')
    all_keys = list(data.keys())
    print('keys: ', all_keys)
    for k in all_keys:
        if isinstance(data[k], str):
            print(f'{k}: {data[k]}')
        elif isinstance(data[k], list):
            np_arr = np.array(data[k])
            print(f'{k}: {np_arr.shape}')
        else:
            print(f'{k}: {type(data[k])}')


if __name__ == '__main__':
    res = load_file_paths('data/emulated', 2)
    print(res[0:5])
    print(res[-5:-1])
    play_with_one_json(res[0])