import matplotlib.pyplot as plt

def read_log_file(filename):
    sizes = []
    times = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            size = int(parts[0].split(": ")[1])
            time = float(parts[1].split(": ")[1].split(" ")[0])
            sizes.append(size)
            times.append(time)
    return sizes, times

def plot_execution_times():
    best_case_sizes, best_case_times = read_log_file("best_case_log.txt")
    worst_case_sizes, worst_case_times = read_log_file("worst_case_log.txt")
    average_case_sizes, average_case_times = read_log_file("average_case_log.txt")
    
    plt.figure(figsize=(10, 6))
    plt.plot(best_case_sizes, best_case_times, 'g', label='Best Case', marker='o')
    plt.plot(worst_case_sizes, worst_case_times, 'r', label='Worst Case', marker='x')
    plt.plot(average_case_sizes, average_case_times, 'b', label='Average Case', marker='s')
    
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Linear Search Execution Time Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_execution_times()
