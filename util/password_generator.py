import string
import argparse
import random

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

def generate_password(special_characters: bool = True, password_length: int = 10):
    characters = (
        list(string.ascii_lowercase) + list(string.ascii_uppercase) + SPECIAL_CHARACTERS
        if special_characters is True
        else list(string.ascii_lowercase) + list(string.ascii_uppercase)
    )
    mixed = [
        characters[random.randint(0, len(characters) - 1)]
        for _ in range(0, len(characters))
    ]
    password = "".join(
        [mixed[random.randint(0, len(mixed) - 1)] for _ in range(0, password_length)]
    )
    return password


def main():
    parser = argparse.ArgumentParser(
        prog="PasswordGenerator", description="Generates random passwords"
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        action="store",
        dest="length",
        required=False,
        default=10,
        help="How many characters the password will have",
    )
    parser.add_argument(
        "-s",
        "--special",
        action="store_true",
        dest="special",
        required=True,
        help="does It include special characters?",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        action="store",
        dest="counter",
        required=False,
        default=1,
        help="How many passwords will be generated",
    )
    args = parser.parse_args()
    return [generate_password(special_characters=args.special, password_length=args.length) for _ in range(0, args.counter)]

if __name__ == "__main__":
    res = main()
    print(f"Passwords Generated: {'\n'.join(res)}")
