import getopt
import sys

from board import Board


def print_usage():
    print("Usage:")
    print("  python board.py -f <input-file> \t Loads starting board from file.")
    print()
    print("Options:")
    print("  -h \t Show this help message and exit.")
    print("  -f, --file \t File to load.")


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:", ["file="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    board = None

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-f", "--file"):
            board = Board(file_name=arg)

    if not board:
        board = Board(height=20, width=40)

    board.run()


if __name__ == "__main__":
    main(sys.argv[1:])
