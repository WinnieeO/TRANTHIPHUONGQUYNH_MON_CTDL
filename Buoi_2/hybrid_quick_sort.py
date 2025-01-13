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

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    quick_sort_hybrid(arr, 0, len(arr) - 1)
    print("Ket qua Quick Sort: ", arr)