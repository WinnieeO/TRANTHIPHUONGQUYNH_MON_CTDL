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
        
def insertion_sort(arr, low, high):
    for i in range (low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort_hybrid(arr, low, high):
    while low < high:
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            p = partition(arr, low, high)
            if p - low < high - p:
                quick_sort_hybrid(arr, low, p - 1)
                low = p + 1
            else:
                quick_sort_hybrid(arr, p + 1, high)
                if p - low < high - p:
                    quick_sort_hybrid(arr, low, p - 1)
                    low = p + 1
                else:
                    quick_sort_hybrid(arr, p + 1, high)
                    high = p - 1

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

# Ham tao mang ngau nhien
def generate_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

if __name__ == "__main__":
    # Su dung Quick Sort Hybrid
    arr = generate_random_array(5000)
    arr_hybrid = arr.copy()
    start_time = time.time()
    quick_sort_hybrid(arr_hybrid, 0, len(arr_hybrid) - 1)
    hybrid_time = time.time() - start_time
    print(f"Thoi gian chay Quick Sort Hybrid: {hybrid_time:.6f}s")

    # Su dung Quick Sort
    arr_standard = arr.copy()
    start_time = time.time()
    quick_sort(arr_standard, 0, len(arr_standard) - 1)
    standard_time = time.time() - start_time
    print(f"Thoi gian chay Quick Sort: {standard_time:.6f}s")