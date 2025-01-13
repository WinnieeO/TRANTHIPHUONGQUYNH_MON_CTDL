#include <iostream>
#include <vector>
using namespace std;

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

int median_of_three(vector<int>& arr, int low, int high){
    int mid = low + (high - low) / 2;
    if (arr[low] > arr[mid])
        swap(arr[low], arr[mid]);
    if (arr[low] > arr[high])
        swap(arr[low], arr[high]);
    if (arr[mid] > arr[high])
        swap(arr[mid], arr[high]);
    return mid;
}

int partition_median(vector<int>& arr, int low, int high){
    int median = median_of_three(arr, low, high);
    swap(arr[median], arr[high]);
    return partitionFunc(arr, low, high);
}

void quickSort_median(vector<int>& arr, int low, int high){
    if (low < high){
        int p = partition_median(arr, low, high);
        quickSort_median(arr, low, p - 1);
        quickSort_median(arr, p + 1, high);
    }
}

int main(){
    vector<int> arr = {5, 2, 9, 1, 5, 6};
    quickSort_median(arr, 0, arr.size() - 1);
    cout << "Ket qua Quick Sort: ";
    for (int x: arr)
        cout << x << " ";
    cout << endl;
    return 0;
}