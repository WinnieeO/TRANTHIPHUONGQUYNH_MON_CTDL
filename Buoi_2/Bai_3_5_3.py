import random
import time

def partition(arr, low, high):
    pivot = arr[high] # Chon pivot la phan tu cuoi
    i = low - 1       # Chi so nho hon pivot
    for j in range (low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Hoan doi arr[i] va arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Hoan doi pivot vao vi tri dung
    return i + 1
        
def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high) # Tim vi tri pivot
        quick_sort(arr, low, p - 1)   # Sap xep phan ben trai cua pivot
        quick_sort(arr, p + 1, high)  # Sap xep phan ben phai cua pivot

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def quick_sort_randomized(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)
        quick_sort_randomized(arr, low, p - 1)
        quick_sort_randomized(arr, p + 1, high)

# Ham tao mang ngau nhien
def generate_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

if __name__ == "__main__":
     # Su dung Quick Sort Hybrid
    arr = generate_random_array(5000)
    arr_random = arr.copy()
    start_time = time.time()
    quick_sort_randomized(arr_random, 0, len(arr_random) - 1)
    random_time = time.time() - start_time
    print(f"Thoi gian chay Quick Sort Hybrid: {random_time:.6f}s")

    # Su dung Quick Sort
    arr_standard = arr.copy()
    start_time = time.time()
    quick_sort(arr_standard, 0, len(arr_standard) - 1)
    standard_time = time.time() - start_time
    print(f"Thoi gian chay Quick Sort: {standard_time:.6f}s")