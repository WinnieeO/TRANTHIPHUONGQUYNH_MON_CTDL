class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Thêm vào đầu - O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Thêm vào cuối - O(n)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:  # Sửa lỗi so sánh sai
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next  # Sửa lỗi gán sai
        current.next = new_node

    # 3. Xóa node đầu - O(1)
    def delete_first(self):
        if self.head:
            self.head = self.head.next

    # 4. Xóa node có giá trị cụ thể - O(n)
    def delete_node(self, key):  # Sửa lỗi tên hàm
        current = self.head

        # Nếu node đầu chứa giá trị cần xóa
        if current and current.data == key:
            self.head = current.next
            return
        
        # Tìm node cần xóa
        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next  # Sửa lỗi thiếu dòng lệnh duyệt

    # 5. Tìm kiếm - O(n)
    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

    # 6. Duyệt danh sách - O(n)
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next  # Sửa lỗi gán sai
        print("None")

# Sử dụng danh sách liên kết
if __name__ == "__main__":
    llist = LinkedList()

    # Thêm các phần tử
    llist.insert_at_beginning(10)
    llist.insert_at_end(20)
    llist.insert_at_beginning(5)
    llist.insert_at_end(30)

    # In danh sách
    print("Danh sách liên kết: ")
    llist.traverse()  # Output: 5 -> 10 -> 20 -> 30 -> None

    # Tìm kiếm
    print("Vị trí của 20: ", llist.search(20))  # Output: 2

    # Xóa phần tử
    llist.delete_node(20)  # Sửa lỗi tên hàm
    print("Sau khi xóa 20: ")
    llist.traverse()  # Output: 5 -> 10 -> 30 -> None
