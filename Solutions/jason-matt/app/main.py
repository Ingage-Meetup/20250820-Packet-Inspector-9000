import sys
from utils import bulk_filter


def main():
    if len(sys.argv) < 2:
        print("whoops, need a max")
        sys.exit(1)
    max_packet: int = int(sys.argv[1])
    print(list(bulk_filter(max_packet)))


if __name__ == "__main__":
    main()
