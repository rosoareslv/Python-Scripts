"""
Module Name: password_generator
Description: Password Generator
Author: Rodrigo Soares
Date: 2025/04/27
Python Version: 3.12.3
"""

import string
import argparse
import random

LENGTH = 32
PASSWORDS_COUNT = 1

SPECIAL_CHARACTERS = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "*",
    "+",
    "-",
    ":",
    ";",
    "=",
    "?",
    "@",
    "_",
]


def get_parameters(parser):
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        action="store",
        dest="length",
        required=False,
        default=LENGTH,
        help="How many characters the password will have",
    )
    parser.add_argument(
        "-s",
        "--special",
        action="store_true",
        dest="special",
        required=False,
        help="does It include special characters?",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        action="store",
        dest="counter",
        required=False,
        default=PASSWORDS_COUNT,
        help="How many passwords will be generated",
    )
    parser.parse_args()
    


def generate_password(args):
    characters = (
        list(string.ascii_lowercase) + list(string.ascii_uppercase) + SPECIAL_CHARACTERS
        if args.special is True
        else list(string.ascii_lowercase) + list(string.ascii_uppercase)
    )
    mixed = [
        characters[random.randint(0, len(characters) - 1)]
        for _ in range(0, len(characters))
    ]
    password = "".join(
        [mixed[random.randint(0, len(mixed) - 1)] for _ in range(0, args.length)]
    )
    return password


def main():
    parser = argparse.ArgumentParser(
        prog="PasswordGenerator", description="Generates random passwords"
    )
    get_parameters(parser)
    args = parser.parse_args()
    for _ in range(0, args.counter):
        print(generate_password(args))


if __name__ == "__main__":
    main()
