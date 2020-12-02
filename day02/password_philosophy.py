#!/usr/bin/env python3

import sys


def password_policy_file_reader(filename):
    with open(filename) as file_object:
        policy = list()
        for line in file_object:
            items = line.split(" ")  # should really use parse()
            policy.append(
                {
                    "min": int(items[0].split("-")[0]),
                    "max": int(items[0].split("-")[1]),
                    "character": items[1][:-1],  # remove trailing colon
                    "password": items[2][:-1],  # remove trailing newline
                }
            )
        return policy


def count_valid_passwords_q1(policy):
    valid = 0
    for item in policy:
        count = item["password"].count(item["character"])
        if count >= item["min"] and count <= item["max"]:
            valid += 1
    return valid


def count_valid_passwords_q2(policy):
    valid = 0
    for item in policy:
        if bool(item["password"][item["min"] - 1] == item["character"]) != bool(
            item["password"][item["max"] - 1] == item["character"]
        ):  # xor
            valid += 1
    return valid


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input file> <policy type (1 or 2)>")
    sys.exit(1)

filename = str(sys.argv[1])
policy_type = int(sys.argv[2])
policy = password_policy_file_reader(filename)
passwords = len(policy)

if policy_type == 1:
    valid_passwords = count_valid_passwords_q1(policy)
elif policy_type == 2:
    valid_passwords = count_valid_passwords_q2(policy)
else:
    print("Invalid policy type. State 1 or 2.")
    sys.exit(1)

print(f"Found {valid_passwords} out of {passwords} in {filename}.")
