import os
import sys
import time


def main():
    pass


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"\nTask is executed in {elapsed:0.2f} seconds.")
