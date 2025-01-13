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

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    quick_sort(arr, 0, len(arr) - 1)
    print("Ket qua Quick Sort: ", arr)