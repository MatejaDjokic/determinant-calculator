from src.determinant2 import determinant2
from src.determinant3 import determinant3
from src.system2 import system2
from src.system3 import system3
from src.install import install
from src.test import test
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Determinant Calculator")

    parser.add_argument('-d2', '--determinant2', action='store_true',
                        help='2nd order determinant')

    parser.add_argument('-d3', '--determinant3', action='store_true',
                        help='3nd order determinant')

    parser.add_argument('-s2', '--system2', action='store_true',
                        help='system with 2 variables')

    parser.add_argument('-s3', '--system3', action='store_true',
                        help='system with 3 variables')

    parser.add_argument('-i', '--install', action='store_true',
                        help='installs the dependencies')

    parser.add_argument('-t', '--test', action='store_true',
                        help='for testing purposes')

    args = parser.parse_args()

    try:
        if args.determinant2:
            determinant2()
        elif args.determinant3:
            determinant3()
        elif args.system2:
            system2()
        elif args.system3:
            system3()
        elif args.install:
            install()
        elif args.test:
            test()
        else:
            print("Use -h or --help for usage information.")
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
