def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Hoan doi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Neu khong co hoan doi nao, mang da duoc sap xep
        if not swapped:
            break

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5]
    bubble_sort(arr)
    print("Ket qua sau khi Bubble Sort: ", arr)