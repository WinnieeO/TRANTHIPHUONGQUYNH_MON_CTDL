
        p = partition!(arr, low, high) # Tim vi tri pivot
        quick_sort!(arr, low, p - 1)   # Sap xep phan ben trai cua pivot
        quick_sort!(arr, p + 1, high)  # Sap xep phan ben phai cua pivot
    end