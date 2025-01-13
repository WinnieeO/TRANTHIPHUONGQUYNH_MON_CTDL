import random

def partition(arr, low, high):
    pivot = arr[high] # Chon pivot la phan tu cuoi
    i = low - 1       # Chi so nho hon pivot
    for j in range (low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Hoan doi arr[i] va arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Hoan doi pivot vao vi tri dung
    return i + 1
        
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def quick_sort_randomized(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)
        quick_sort_randomized(arr, low, p - 1)
        quick_sort_randomized(arr, p + 1, high)

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    quick_sort_randomized(arr, 0, len(arr) - 1)
    print("Ket qua Quick Sort: ", arr)