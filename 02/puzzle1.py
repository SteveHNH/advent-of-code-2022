#!/usr/bin/python

# This solution feels very much like using simple
# tools to get to a solution. Not real happy with it, but it
# got me the win :P

scores = {"X": 1,
          "Y": 2,
          "Z": 3,
          }


values = {"A": 1,
          "B": 2,
          "C": 4,
          "X": 8,
          "Y": 16,
          "Z": 32,
          }

winner = [
        12,
        17,
        34,
        ]

draw = [
        9,
        18,
        36
        ]


def get_strategy(path):
    f = open(path, "r")
    lines = f.readlines()

    rounds = []
    for line in lines:
        rounds.append(line.split())

    return rounds


def convert_score(arr):
    converted_round = [values[arr[0]], values[arr[1]]]
    return converted_round


def main():
    total_scores = []
    rounds = get_strategy("./input")
    print(rounds)
    for round in rounds:
        round_score = []
        values = convert_score(round)
        round_score.append(scores[round[-1]])
        result = sum(values)
        if result in winner:
            round_score.append(6)
        elif result in draw:
            round_score.append(3)
        else:
            round_score.append(0)
        total_scores.append(sum(round_score))
    print("Part 1: " + str(sum(total_scores)))

    # part 2
    # This is so gnarly but it got me there
    part_2_scores = []
    for round in rounds:
        round_score = []
        values = convert_score(round)
        if values[-1] == 8:
            round_score.append(0)
            if values[0] == 1:
                round_score.append(3)
            if values[0] == 2:
                round_score.append(1)
            if values[0] == 4:
                round_score.append(2)
        if values[-1] == 16:
            round_score.append(3)
            if values[0] == 1:
                round_score.append(1)
            if values[0] == 2:
                round_score.append(2)
            if values[0] == 4:
                round_score.append(3)
        if values[1] == 32:
            round_score.append(6)
            if values[0] == 1:
                round_score.append(2)
            if values[0] == 2:
                round_score.append(3)
            if values[0] == 4:
                round_score.append(1)
        part_2_scores.append(sum(round_score))

    print("Part 2: " + str(sum(part_2_scores)))


if __name__ == "__main__":
    main()
