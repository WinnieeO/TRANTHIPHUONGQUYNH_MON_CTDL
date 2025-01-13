def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left : left + n1]
    R = arr[mid + 1 : mid + 1 + n2]

    i, j = 0, 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Sao chep phan con lai cua L, neu co
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Sao chep phan con lai cua R, neu co
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # Di chuyen cac phan tu lon hon key sang phai
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Chen key vao vi tri dung
        arr [j + 1] = key

def merge_sort_hybrid(arr, left, right):
    if right - left + 1 < 10:
        insertion_sort(arr, left, right)
    elif left < right:
        mid = (left + right) // 2
        merge_sort_hybrid(arr, left, mid)
        merge_sort_hybrid(arr, mid + 1, right)
        merge(arr, left, mid, right)

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    merge_sort_hybrid(arr, 0, len(arr) - 1)
    print("Ket qua Merge Sort: ", arr)