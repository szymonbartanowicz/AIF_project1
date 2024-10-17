import csv
from collections import defaultdict
import re

stats = defaultdict(lambda: {'sum': [0, 0, 0, 0], 'count': 0})


def get_grid_size(filename):
    match = re.search(r'(\d+)x\1', filename)
    if match:
        return match.group(0)
    return "Unknown"


with open('stats_output.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')

    for row in reader:
        stat1 = int(row[0])
        stat2 = int(row[1])
        stat3 = int(row[2])
        stat4 = int(row[3])
        algorithm = row[4]
        filename = row[5]

        grid_size = get_grid_size(filename)

        key = (algorithm, grid_size)
        stats[key]['sum'][0] += stat1
        stats[key]['sum'][1] += stat2
        stats[key]['sum'][2] += stat3
        stats[key]['sum'][3] += stat4
        stats[key]['count'] += 1

for (algorithm, grid_size), data in stats.items():
    count = data['count']
    averages = [s / count for s in data['sum']]
    print(f"{algorithm} ({grid_size}): Averages -> {averages}")
