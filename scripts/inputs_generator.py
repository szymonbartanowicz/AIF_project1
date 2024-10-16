import random
import os
import shutil
from constants import MAP_SIZES


class MapGenerator:
    def __init__(self, size):
        self.size = size

    def generate_matrix(self):
        return [[random.randint(1, 9) for _ in range(self.size)] for _ in range(self.size)]

    def generate_start(self):
        row = 0
        col = 0
        position = 0

        return row, col, position

    def generate_target(self):
        row = self.size - 1
        col = self.size - 1
        position = 8

        return row, col, position

    def save_to_file(self, matrix, start, target, filename):
        with open(filename, 'w') as f:
            f.write(f"{self.size} {self.size}\n")
            for row in matrix:
                f.write(" ".join(map(str, row)) + "\n")
            f.write(f"{start[0]} {start[1]} {start[2]}\n")
            f.write(f"{target[0]} {target[1]} {target[2]}\n")


def main():
    sizes = MAP_SIZES
    output_dir = "../inputs/"

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    for size in sizes:
        generator = MapGenerator(size)
        for i in range(10):
            matrix = generator.generate_matrix()
            start = generator.generate_start()
            target = generator.generate_target( )
            filename = os.path.join(output_dir, f"{size}x{size}_{i + 1}.txt")
            generator.save_to_file(matrix, start, target, filename)


if __name__ == "__main__":
    main()
