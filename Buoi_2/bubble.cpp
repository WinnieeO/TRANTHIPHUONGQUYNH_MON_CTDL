#include <iostream>
#include <vector>
using namespace std;

// Ham Bubble Sort
void bubbleSort(vector<int>& arr){
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; i++){
        swapped = false;
        for (int j = 0; j < n - 1 - i; j++){
            if (arr[j] > arr[j + 1]){
                // Hoan doi
                int temp = arr[i];
                arr[i] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        // Neu khong co hoan doi nao, mang da duoc sap xep
        if (!swapped)
            break;
    }
}

int main(){
    vector<int> arr = {5, 2, 9, 1, 5};
    bubbleSort(arr);
    cout << "Ket qua sau Bubble Sort: ";
    for (int x: arr)
        cout << x << " ";
    cout << endl;
    return 0;
}