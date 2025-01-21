#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(){
    queue<string> queue;

    // Enqueue các phần tử vào hàng đợi
    queue.push("Tai Lieu 1");
    cout << "Da them 'Tai Lieu 1' vao hang doi." << endl;
    queue.push("Tai Lieu 2");
    cout << "Da them 'Tai Lieu 2' vao hang doi." << endl;
    queue.push("Tai Lieu 3");
    cout << "Da them 'Tai Lieu 3' vao hang doi." << endl;

    // Hiển thị phần tử ở đầu hàng đợi
    cout << "Phan tu o dau hang doi: " << queue.front() << endl; // Output: Tai Lieu 1

    // Dequeue phần tử khỏi hàng đợi
    queue.pop();
    cout << "Da lay phan tu ra khoi hang doi." << endl;

    // Hiển thị phần tử ở đầu hàng đợi sau khi dequeue
    cout << "Phan tu o dau hang doi sau khi dequeue: " << queue.front() << endl; // Output: Tai Lieu 2

    // Kiểm tra hàng đợi có trống không
    if (queue.empty()){
        cout << "Hang doi trong!" << endl;
    }
    else{
        cout << "Hang doi khong trong." << endl; // Output: Hang doi khong trong.
    }

    return 0;
}
