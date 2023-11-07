import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        rows = [l for l in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, 'w') as f1:
        json.dump(rows, f1, indent=4, ensure_ascii=True)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
