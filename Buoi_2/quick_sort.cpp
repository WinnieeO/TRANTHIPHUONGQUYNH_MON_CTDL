#include <iostream>
#include <vector>
using namespace std;

// Ham Partition: Dua pivot ve vi tri dung va sap xep cac phan tu
int partitionFunc(vector<int>& arr, int low, int high){
    int pivot = arr[high]; // Chon pivot la phan tu cuoi
    int i = low - 1;       // Chi so nho hon pivot

    for (int j = low; j < high; j++){
        if (arr[j] <= pivot){
            i++;
            // Hoan doi arr[i] va arr[j]
            int temp = arr[j];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Hoan doi pivot voi arr[i + 1] de dua pivot vao vi tri dung
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1; // Vi tri cua pivot
}

// Ham Quick Sort
void quickSort(vector<int>& arr, int low, int high){
    if (low < high){
        // Tim vi tri pivot
        int p = partitionFunc(arr, low, high);

        // Goi de quy Quick Sort cho hai phan ben trai va ben phai cua pivot
        quickSort(arr, low, p - 1);
        quickSort(arr, p + 1, high);
    }
}

int main(){
    vector<int> arr = {5, 2, 9, 1, 5, 6};
    quickSort(arr, 0, arr.size() - 1);
    cout << "Ket qua Quick Sort: ";
    for (int x: arr)
        cout << x << " ";
    cout << endl;
    return 0;
}