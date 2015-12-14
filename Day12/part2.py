import re, json

with open('input.txt') as f:
    lines=f.readline()

def explore(collection):
    if type(collection)==dict:
        if any('red' in [k, v] for k, v in collection.items()): return 0
        return sum(explore(v) for k, v in collection.items())

    elif type(collection)==list:
        return sum(explore(item) for item in collection)

    else:
        try:
            return int(collection)
        except ValueError:
            return 0

obj = json.loads(lines)
print(explore(obj))
