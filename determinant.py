import os
from src.order2 import prompt2, calc2
from src.order3 import prompt3, calc3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Determinant Calculator")

    parser.add_argument('-o2', '--order2', action='store_true',
                        help='2nd order determinant')

    parser.add_argument('-o3', '--order3', action='store_true',
                        help='3nd order determinant')

    parser.add_argument('-i', '--install', action='store_true',
                        help='installs the dependencies')

    args = parser.parse_args()

    if args.order2:
        print(f"\nEquals: {calc2(prompt2())}")
    elif args.order3:
        print(f"\nEquals: {calc3(prompt3())}")
    elif args.install:
        install()
    else:
        print("Use -h or --help for usage information.")


def install():
    os.system(r"pip install -r requirements.txt")


if __name__ == "__main__":
    main()
