import argparse


def main():
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument(
        "name",
        nargs="?",
        default="world",
        help="the name to greet (default: world)",
    )
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="print the greeting in uppercase",
    )
    parser.add_argument(
        "--times",
        type=int,
        default=1,
        help="number of times to print the greeting (default: 1)",
    )
    args = parser.parse_args()

    if args.times < 1:
        parser.error("--times must be at least 1")

    greeting = f"Hello, {args.name}!"
    if args.uppercase:
        greeting = greeting.upper()
    for _ in range(args.times):
        print(greeting)


if __name__ == "__main__":
    main()
