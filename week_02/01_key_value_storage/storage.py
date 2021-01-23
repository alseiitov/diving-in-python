import os
import json
import tempfile
import argparse


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    return parser.parse_args()


def read_file_to_dict(path):
    if not os.path.exists(storage_path):
        return {}
    with open(path, 'r') as f:
        data = f.read()
        return json.loads(data)


def write_dict_to_file(path, dict):
    with open(path, 'w') as file:
        json_data = json.dumps(storage)
        file.write(json_data)


def print_values(storage, key):
    if args.key in storage:
        print(*storage[key], sep=', ')
    else:
        print()


def add_value(storage, key, val):
    if key not in storage:
        storage[key] = []
        storage[key].append(val)
    else:
        storage[key].append(val)


def print_or_add(storage, storage_path, args):
    if args.val is None:
        print_values(storage, args.key)
    else:
        add_value(storage, args.key, args.val)
        write_dict_to_file(storage_path, storage)


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
storage = read_file_to_dict(storage_path)
args = read_args()
print_or_add(storage, storage_path, args)
