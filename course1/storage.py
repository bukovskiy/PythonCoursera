import os
import tempfile
import argparse
import json

def read_dict(string):
    if not string:
        return {}
    else:
        return json.loads(string)


def write_dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)
    return json.dumps(dictionary, separators=(",", ":"))

def show(dict, key):
    if not dict[key]:
        return None
    else:
        values = dict[key]
        return ", ".join(values)

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data1')
#storage_path = "log.txt"
if not os.path.exists(storage_path):
    file = open(storage_path, "w+")
    file.close()

if args.key and args.value:
    with open(storage_path, 'r') as f:
        f.seek(0)
        read = f.read()
#        print(read)
        dic = read_dict(read)
    with open(storage_path, 'w') as f:
        load = write_dict(dic, args.key, args.value)
#        print(load)
        f.write(load)

elif args.key and not args.value:
    with open(storage_path, 'r') as f:
        f.seek(0)
        if not f.read():
            print(None)
        else:
            f.seek(0)
            dictionary = json.loads(f.read())
            print(show(dictionary, args.key))
#   print(", ".join(dictionary[args.key]))


