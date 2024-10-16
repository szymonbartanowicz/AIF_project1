import csv
from collections import defaultdict
import re

# Initialize a dictionary to store totals and counts for each (algorithm, grid size)
stats = defaultdict(lambda: {'sum': [0, 0, 0, 0], 'count': 0})


# Function to extract grid size from the filename
def get_grid_size(filename):
    match = re.search(r'(\d+)x\1', filename)  # Regex to find n x n pattern
    if match:
        return match.group(0)  # Return grid size as n x n
    return "Unknown"


# Read the TSV file
with open('stats_output.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')

    for row in reader:
        # Extract the statistics and algorithm
        stat1 = int(row[0])
        stat2 = int(row[1])
        stat3 = int(row[2])
        stat4 = int(row[3])
        algorithm = row[4]
        filename = row[5]

        # Extract grid size from the file name
        grid_size = get_grid_size(filename)

        # Update the sums and count for the (algorithm, grid size) pair
        key = (algorithm, grid_size)
        stats[key]['sum'][0] += stat1
        stats[key]['sum'][1] += stat2
        stats[key]['sum'][2] += stat3
        stats[key]['sum'][3] += stat4
        stats[key]['count'] += 1

# Calculate and display averages for each algorithm and grid size
for (algorithm, grid_size), data in stats.items():
    count = data['count']
    averages = [s / count for s in data['sum']]
    print(f"{algorithm} ({grid_size}): Averages -> {averages}")
