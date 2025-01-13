function insertion_sort!(arr)
    n = length(arr)
    for i in 2:n
        key = arr[i]
        j = i - 1
        # Di chuyen cac phan tu lon hon key sang phai
        while j >= 1 && arr[j] > key
            arr[j + 1] = arr[j]
            j -= 1
        end
        # Chen key vao vi tri dung
        arr[j + 1] = key
    end
    return arr
end

# Test
arr = [5, 2, 9, 1, 5]
insertion_sort!(arr)
println("Ket qua sau Insertion Sort: ", arr)