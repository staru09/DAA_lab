import matplotlib.pyplot as plt
import pandas as pd
import re

log_file_path = "execution_times_long.log"
data = []

with open(log_file_path, "r") as file:
    for line in file:
        match = re.search(r"Array size = (\d+), Bubble sort took (\d+\.\d+) seconds", line)
        if match:
            array_size = int(match.group(1))
            runtime = float(match.group(2))
            data.append((array_size, runtime))

df = pd.DataFrame(data, columns=["Array Size", "Runtime"])

plt.figure(figsize=(10, 6))
plt.plot(df["Array Size"], df["Runtime"], marker='o', linestyle='-', color='b')
plt.title("Bubble Sort Execution Time vs. Number of Inputs")
plt.xlabel("Number of Inputs (Array Size)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.show()
