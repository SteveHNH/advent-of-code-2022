#!/usr/bin/python3

# Advent of Code - Day 1

def get_lines(path):
    f = open(path, "r")
    lines = f.readlines()
    return lines


def main():
    values = []
    totals = []
    arr = []

    lines = get_lines("./input.txt")

    for line in lines:
        if line.strip() != "":
            arr.append(int(line))
        else:
            values.append(arr)
            arr = []

    for _set in values:
        totals.append(sum(_set))

    sorted_totals = sorted(totals)
    # part 1
    print("Top Calories: " + str(sorted_totals[-1]))
    # part 2
    print("Top 3 Calories: " + str(sum(sorted_totals[-3:])))


if __name__ == "__main__":
    main()
