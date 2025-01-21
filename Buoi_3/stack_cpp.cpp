#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    stack<string> stack;

    // Push các phần tử vào ngăn xếp
    stack.push("Sach A");
    cout << "Da them 'Sach A' vao ngan xep." << endl;
    stack.push("Sach B");
    cout << "Da them 'Sach B' vao ngan xep." << endl;
    stack.push("Sach C");
    cout << "Da them 'Sach C' vao ngan xep." << endl;

    // Hiển thị phần tử ở đỉnh ngăn xếp
    cout << "Phan tu o dinh ngan xep: " << stack.top() << endl; // Output: Sách C

    // Pop phần tử khỏi ngăn xếp
    stack.pop();
    cout << "Da lay phan tu ra khoi ngan xep." << endl;

    // Hiển thị phần tử ở đỉnh ngăn xếp sau khi pop
    cout << "Phan tu o dinh ngan xep sau khi pop: " << stack.top() << endl; // Output: Sách B

    // Kiểm tra ngăn xếp có trống không
    if (stack.empty()){
        cout << "Ngan xep trong!" << endl;
    }
    else{
        cout << "Ngan xep khong trong." << endl; // Output: Ngăn xếp không trống.
    }
    return 0;
}