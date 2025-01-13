function bubble_sort!(arr)
    n = length(arr)
    for i in 1:(n - 1)
        swapped = false
        for j in 1:(n - 1)
            if arr[j] > arr[j + 1]
                # Hoan doi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = true
            end
        end
        # Neu khong co hoan doi nao, mang da duoc sap xep
        if !swapped
            break
        end
    end
    return arr
end

# Test
arr = [5, 2, 9, 1, 5]
bubble_sort!(arr)
println("Ket qua sau khi Bubble Sort: ", arr)