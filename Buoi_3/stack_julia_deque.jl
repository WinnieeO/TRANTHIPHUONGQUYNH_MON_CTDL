using DataStructures

struct Stack
    elements::Deque{Any} # Sử dụng Deque để lưu trữ phần tử
end

Stack() = Stack(Deque{Any}()) # Constructor khởi tạo ngăn xếp rỗng

# Hàm thêm phần tử vào ngăn xếp
function push!(s::Stack, item)
    Base.push!(s.elements, item) # Dùng Base.push! để xử lý deque
    println("Đã thêm '$item' vào ngăn xếp.")
end

# Hàm loại bỏ phần tử khỏi ngăn xếp
function pop!(s::Stack)
    if !isempty(s.elements)
        item = Base.pop!(s.elements) # Loại bỏ phần tử từ cuối deque
        println("Đã lấy '$item' ra khỏi ngăn xếp.")
        return item
    else
        println("Ngăn xếp trống!")
        return nothing
    end
end

# Hàm xem phần tử ở đỉnh ngăn xếp
function peek(s::Stack)
    if !isempty(s.elements)
        return last(s.elements) # Lấy phần tử cuối cùng
    else
        println("Ngăn xếp trống!")
        return nothing
    end
end

# Hàm kiểm tra ngăn xếp rỗng
function is_empty(s::Stack)
    return isempty(s.elements)
end

# Hàm in nội dung ngăn xếp
function display(s::Stack)
    println("Ngăn xếp (đỉnh đến đáy): ", reverse(collect(s.elements)))
end

# Minh họa sử dụng ngăn xếp với Deque
function main()
    stack = Stack()
    push!(stack, "Sách A")
    push!(stack, "Sách B")
    push!(stack, "Sách C")
    display(stack) # Output: Ngăn xếp (đỉnh đến đáy): ["Sách C", "Sách B", "Sách A"]

    top_item = peek(stack)
    println("Phần tử ở đỉnh ngăn xếp: ", top_item) # Output: Sách C
    
    pop!(stack)
    display(stack) # Output: Ngăn xếp (đỉnh đến đáy): ["Sách B", "Sách A"]
    println("Ngăn xếp có trống không? ", is_empty(stack) ? "Có" : "Không") # Output: Không
end

main()