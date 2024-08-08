import random
import timeit

def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def generate_random_array(size):
    lower_bound = 1
    upper_bound = 1000
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def log_execution_time(filename, size, execution_time):
    with open(filename, "a") as log_file:
        log_file.write(f"Array Size: {size}, Execution Time: {execution_time:.10f} seconds\n")

if __name__ == "__main__":
    array_size = int(input("Enter the size of the array: "))
    numbers = generate_random_array(array_size)
    print(f"Generated array: {numbers}")
    
    # Best Case: Target is the first element
    target = numbers[0]
    best_case_time = timeit.timeit(lambda: linear_search(numbers, target), number=1)
    log_execution_time("best_case_log.txt", array_size, best_case_time)
    print(f"Best case time: {best_case_time:.10f} seconds.")
    
    # Worst Case: Target is the last element
    target = numbers[-1]
    worst_case_time = timeit.timeit(lambda: linear_search(numbers, target), number=1)
    log_execution_time("worst_case_log.txt", array_size, worst_case_time)
    print(f"Worst case time: {worst_case_time:.10f} seconds.")

    # Average Case: Target is a random element
    random_index = random.randint(0, array_size - 1)
    target = numbers[random_index]
    average_case_time = timeit.timeit(lambda: linear_search(numbers, target), number=1)
    log_execution_time("average_case_log.txt", array_size, average_case_time)
    print(f"Average case time: {average_case_time:.10f} seconds.")
