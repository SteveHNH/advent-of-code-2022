#!/usr/bin/python

##
# Advent of Code - Day 3
##

import string

alphabet = list(string.ascii_letters)


def get_input(path):
    with open(path, "r") as f:
        data = f.readlines()
    return data


def get_alphabet_map():
    alphabet_scores = {}
    loop_count = 1
    for i in alphabet:
        alphabet_scores[i] = loop_count
        loop_count += 1
    print(alphabet_scores)
    return alphabet_scores


def part1(data):
    alphabet_scores = get_alphabet_map()
    key_items = []
    for line in data:
        line = line.strip()
        size = len(line)
        size = int(size / 2)
        sack1 = line[:-size]
        sack2 = line[-size:]
        for i in set(sack1):
            if i in set(sack2):
                key_items.append(alphabet_scores[i])
    print("Part 1: " + str(sum(key_items)))


def part2(data):
    alphabet_scores = get_alphabet_map()
    badges = {}
    chunked_list = list()
    chunk_size = 3
    for i in range(0, len(data), chunk_size):
        chunked_list.append(data[i:i+chunk_size])
    print(chunked_list)
    for chunk in chunked_list:
        if chunk[0].strip() in badges.items():
            break
        for i in set(chunk[0].strip()):
            if i in set(chunk[1].strip()) and i in set(chunk[-1].strip()):
                badges[chunk[0].strip()] = alphabet_scores[i]
    score = 0
    for k, v in badges.items():
        score += v

    print("Part 2: " + str(score))


def main():
    data = get_input("./input")
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
