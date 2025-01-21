#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Stack{
    private:
        vector<string> elements; // Sử dụng vector để lưu trữ phần tử
    public:
        // Thêm phần tử vào ngăn xếp
        void push(const string& item){
            elements.push_back(item);
            cout << "Da them '" << item << "' vao ngan xep." << endl;
        }
        // Loại bỏ phần tử khỏi ngăn xếp
        void pop(){
            if (!isEmpty()){
                string item = elements.back();
                elements.pop_back();
                cout << "Da lay '" << item << "' ra khoi ngan xep." << endl;
            }
            else{
                cout << "Ngan xep trong!" << endl;
            }
        }

        // Xem phần tử ở đỉnh ngăn xếp
        string peek() const{
            if (!isEmpty()){
                return elements.back();
            }
            else{
                throw out_of_range("Ngan xep trong!");
            }
        }

        // Kiểm tra ngăn xếp rỗng
        bool isEmpty() const{
            return elements.empty();
        }

        // Trả về kích thước ngăn xếp
        int size() const{
            return elements.size();
        }

        // In nội dung ngăn xếp từ đỉnh đến đáy
        void display() const{
            cout << "Ngan xep (dinh den day): ";
            for (auto it = elements.rbegin(); it != elements.rend(); ++it)
                cout << *it << " ";
            cout << endl;
        }
};

// Hàm main để minh họa
int main(){
    Stack stack;
    stack.push("Sach A");
    stack.push("Sach B");
    stack.push("Sach C");
    stack.display(); // Output: Ngăn xếp (đỉnh đến đáy): Sách C Sách B Sách A
    
    try{
        cout << "Phan tu o dinh ngan xep: " << stack.peek() << endl; // Output: Sách C
    }
    catch (const out_of_range& e){
        cout << e.what() << endl;
    }

    stack.pop();
    stack.display(); // Ngăn xếp (đỉnh đến đáy): Sách B Sách A

    cout << "Ngan xep co trong khong? " << (stack.isEmpty() ? "Co" : "Khong") << endl; // Output: Không
    return 0;
}