#include <iostream>
#include <vector>
using namespace std;

// Ham Insertion Sort
void insertionSort(vector<int>& arr){
    int n = arr.size();
    for (int i = 1; i < n; i++){
        int key = arr[i];
        int j = i - 1;
        // Di chuyen cac phan tu lon hon key sang phai
        while (j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j];
            j--;
        }
        // Chen key vao vi tri dung
        arr[j + 1] = key;
    }
}

int main(){
    vector<int> arr = {5, 2, 9, 1, 5};
    insertionSort(arr);
    cout << "Ket qua sau Insertion Sort: ";
    for (int x : arr)
        cout << x << " ";
    cout << endl;
    return 0;
}