import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def output(filename):
    with open(f"{current_dir}/{filename}.json", "r") as f:
        data = json.load(f)
    return data