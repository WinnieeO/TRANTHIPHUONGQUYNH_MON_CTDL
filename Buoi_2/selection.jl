function selection_sort!(arr)
    n = length(arr)
    for i in 1:(n-1)
        # Tim chi so cua phan tu nho nhat trong [i..n]
        min_index = i
        for j in (i+1):n
            if arr[j] < arr[min_index]
                min_index = j
            end
        end
        # Hoan doi neu min_index khac i
        if min_index != i
            arr[i], arr[min_index] = arr[min_index], arr[i]
        end
    end
    return arr
end

# Test
arr = [5, 2, 9, 1, 5]
selection_sort!(arr)
println("Ket qua sau Selection Sort: ", arr)