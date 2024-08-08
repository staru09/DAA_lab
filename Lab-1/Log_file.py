import random
import timeit
from datetime import datetime

def bubble_sort(arr):
    for _ in range(len(arr)):
        swapped = False
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swapped = True

        if not swapped:
            break

if __name__ == "__main__":
    array_size = int(input("Enter the size of the array: "))
    
    arr = [random.randint(1, 1000) for _ in range(array_size)]

    print("Original array:")
    print(arr)

    def sort_and_measure():
        bubble_sort(arr.copy())  

    runtime = timeit.timeit(sort_and_measure, number=1)

    print("Sorted array:")
    bubble_sort(arr)  
    print(arr)

    print(f"Bubble sort took {runtime:.6f} seconds")

    with open("execution_times_long.log", "a") as log_file:
        log_file.write(f"{datetime.now()}: Array size = {array_size}, Bubble sort took {runtime:.6f} seconds\n")
