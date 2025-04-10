# include <iostream>
#include <vector>
using namespace std;

// Ham Selection Sort
void  selectionSort(vector<int>& arr){
    int n = arr.size();
    for (int i = 0; i < n - 1; i++){
        // Tim chi so cua phan tu nho nhat trong [i..n-1]
        int minIndex = i;
        for (int j = i + 1; j < n; j++){
            if (arr[j] < arr[minIndex]){
                minIndex = j;
            }
        }
        // Hoan doi neu minIndex khac i
        if (minIndex != i){
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}

int main(){
    vector<int> arr = {5, 2, 9, 1, 5};
    selectionSort(arr);
    cout <<"Ket qua sau Selection Sort: ";
    for (int x : arr)
        cout << x << " ";
    cout << endl;
    return 0;
}