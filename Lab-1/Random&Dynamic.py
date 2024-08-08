import random
import time

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

    arr = [random.randint(1, 100) for _ in range(array_size)]

    print("Original array:")
    print(arr)

    start_time = time.time()

    bubble_sort(arr)

    end_time = time.time()

    exec_time = end_time - start_time

    print("Sorted array:")
    print(arr)
    print(f"Bubble sort took {exec_time:.6f} seconds")