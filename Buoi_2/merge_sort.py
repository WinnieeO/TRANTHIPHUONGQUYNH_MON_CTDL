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
    
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        #Sap xep de quy tung nua
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Tron hai nua da sap xep
        merge(arr, left, mid, right)

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    merge_sort(arr, 0, len(arr) - 1)
    print("Ket qua Merge Sort: ", arr)