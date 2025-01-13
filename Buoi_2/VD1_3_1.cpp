// Tinh Tong Tu 1 Den n
#include <iostream>
using namespace std;

int sum_1_to_n(int n){
    int s = 0; // 1 phep gan
    for (int i = 1; i <= n; i++){ // n lan lap
        s += i; // 1 phep cong va 1 phep gan moi lan gap
    }
    return s;
}

int main(){
    int n = 5;
    cout << "Tong 1.." << n << "= " << sum_1_to_n << endl; // Output: 15
    return 0;
}