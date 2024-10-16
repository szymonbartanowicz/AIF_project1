import os
import sys
sys.path.append('/Users/szymonbartanowicz/studia/udc_1/AIF_project1')
from constants import ALGORITHMS, INPUTS_DIR


def run_all_algorithms(input_folder):
    for algorithm in ALGORITHMS:
        print(f"Running algorithm: {algorithm}")

        for input_file in os.listdir(input_folder):
            input_path = os.path.join(input_folder, input_file)
            if os.path.isfile(input_path):
                os.system(f'python main.py {algorithm} {input_file}')
            else:
                print(f"Warning: '{input_file}' is not a file and will be skipped.")


def main():
    run_all_algorithms(INPUTS_DIR)


if __name__ == "__main__":
    main()
