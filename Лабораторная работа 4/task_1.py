import json


def task() -> float:
    with open('input.json', 'r') as f:
        data = json.load(f)
        return round(sum([d["score"] * d["weight"] for d in data]), 3)

print(task())
