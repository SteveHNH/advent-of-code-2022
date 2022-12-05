#!/usr/bin/python

import re

path = "./input"
sections = []

with open(path, "r") as f:
    for line in f:
        sections.append(line.strip())

regex = r"^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$"

part1 = 0
part2 = 0

for section in sections:
    start1, end1, start2, end2 = re.match(regex, section).groups()
    SET1 = set(range(int(start1), int(end1) + 1))
    SET2 = set(range(int(start2), int(end2) + 1))
    if SET1.issubset(SET2) or SET2.issubset(SET1):
        part1 += 1
    if SET1.intersection(SET2):
        part2 += 1


print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
