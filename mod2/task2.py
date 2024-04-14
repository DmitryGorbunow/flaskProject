import sys

from flask import Flask


# ls -l | python3 mod2/task2.py


def average_file_size():
    lines = sys.stdin.readlines()[1:]
    numbers = []
    for line in lines:
        print(line)
        parts = line.split()
        numbers.append(parts[4])

    numbers = [int(num) for num in numbers]

    total = sum(numbers)

    count = len(numbers)
    return total / count


if __name__ == '__main__':
    print(average_file_size())
