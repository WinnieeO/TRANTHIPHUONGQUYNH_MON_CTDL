def selection_sort(arr):
    n = len(arr)
    for i in range (n - 1):
        # Tim chi so cua phan tu nho nhat trong [i..n - 1]
        min_index = i
        for j in range (i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Hoan doi neu min_index khac i
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5]
    selection_sort(arr)
    print("Ket qua sau Selection Sort: ", arr)