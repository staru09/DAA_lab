import random
import time
import pandas as pd
import matplotlib.pyplot as plt

def generate_random_numbers(size):
    return [random.randint(0, 100000) for _ in range(size)]

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def measure_execution_time(arr, target):
    start_time = time.perf_counter()
    linear_search(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time

def empirical_analysis(sizes):
    best_times = []
    worst_times = []
    average_times = []
    number_of_runs = []

    for run_number, size in enumerate(sizes, start=1):
        arr = generate_random_numbers(size)
        
        # Best case: target is the first element
        target_best = arr[0]
        best_case_time = measure_execution_time(arr, target_best)
        
        # Worst case: target is not in the list
        target_worst = -1  # Ensure this value is not in the list
        worst_case_time = measure_execution_time(arr, target_worst)

        # Average case: target is a middle element in the list
        target_avg = arr[size // 2]
        average_case_time = measure_execution_time(arr, target_avg)

        best_times.append(best_case_time)
        worst_times.append(worst_case_time)
        average_times.append(average_case_time)
        number_of_runs.append(run_number)

        print(f"Run: {run_number}, Size: {size}, Best: {best_case_time:.10f} s, Worst: {worst_case_time:.10f} s, Average: {average_case_time:.10f} s")

    # Create a DataFrame to display results in a table with custom indices
    results = pd.DataFrame({
        'Number of Runs': number_of_runs,
        'Size': sizes,
        'Best Time (s)': best_times,
        'Worst Time (s)': worst_times,
        'Average Time (s)': average_times
    })

    # Format the DataFrame to display numbers in a more readable format
    pd.options.display.float_format = '{:.10f}'.format

    # Display the results table
    print("\nResults Table:")
    print(results)

    # Plot the results
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, best_times, marker='o', linestyle='-', color='g', label='Best Case')
    plt.plot(sizes, worst_times, marker='o', linestyle='-', color='r', label='Worst Case')
    plt.plot(sizes, average_times, marker='o', linestyle='-', color='b', label='Average Case')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Linear Search Execution Time Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()


    return results

# Prompt user for sizes
def get_sizes_from_user():
    sizes = []
    run_number = 1
    while True:
        try:
            size_input = input(f"Enter the size of run {run_number} (or type 'done' to finish): ")
            if size_input.lower() == 'done':
                break
            size = int(size_input)
            sizes.append(size)
            run_number += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'done'.")

    return sizes

sizes = get_sizes_from_user()
results = empirical_analysis(sizes)










