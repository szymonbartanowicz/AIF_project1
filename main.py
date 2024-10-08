import sys
import os
import importlib
from constants import ALGORITHMS, INPUTS_DIR


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <algorithm> <input_file>")
        sys.exit(1)

    algorithm = sys.argv[1]
    input_file = sys.argv[2]

    if algorithm not in ALGORITHMS:
        print(f"Error: '{algorithm}' is not a valid algorithm. Choose from {ALGORITHMS}.")
        sys.exit(1)

    input_path = os.path.join(INPUTS_DIR, input_file)
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_file}' not found in {INPUTS_DIR} folder.")
        sys.exit(1)

    print(f"Algorithm: {algorithm}")
    print(f"Processing file: {input_file}...")

    try:
        algorithm_module = importlib.import_module(f"algorithms.{algorithm}")
        algorithm_module.main(input_path)
    except ModuleNotFoundError:
        print(f"Error: The algorithm '{algorithm}' could not be found in the 'algorithms' folder.")
        sys.exit(1)
    except AttributeError:
        print(f"Error: The module 'algorithms.{algorithm}' does not have a 'main' function.")
        sys.exit(1)


if __name__ == "__main__":
    main()
