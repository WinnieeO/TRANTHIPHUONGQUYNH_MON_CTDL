#include <iostream>
#include <vector>
using namespace std;

// Khai bao bien toan cuc
int mergeSortComparisons = 0;
int quickSortComparisons = 0;

// Ham tron hai mang con da duoc sap xep
void merge(vector<int>& arr, int left, int mid, int right){
    int n1 = mid - left + 1; // Kich thuoc mang con trai
    int n2 = right - mid;    // Kich thuoc mang con phai

    // Tao cac mang tam thoi
    vector<int> L(n1), R(n2);

    // Sao chep du lieu vao mang tam L va R
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Tron hai mang L va R vao arr[left..right]
    int i = 0, j = 0;
    int k = left; // Vi tri gop vao arr
    while (i < n1 && j < n2){
        mergeSortComparisons++; // Tang bien dem so sanh
        if (L[i] <= R[j]){
            arr[k++] = L[i++];
        }
        else{
            arr[k++] = R[j++];
        }
    }

    // Sao chep phan con lai cua L, neu co
    while (i < n1){
        arr[k++] = L[i++];
    }

    // Sao chep phan con lai cua R, neu co
    while (j < n2){
        arr[k++] = R[j++];
    }
}

// Ham Merge Sort
void mergeSort(vector<int>& arr, int left, int right){
    if (left <right){
        int mid = left + (right - left) / 2; // Tom diem giua de chia doi

        // Sap xep de quy tung nua
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Tron hai nua da sap xep
        merge(arr, left, mid, right);
    }
}

// Ham Partition: Dua pivot ve vi tri dung va sap xep cac phan tu
int partitionFunc(vector<int>& arr, int low, int high){
    int pivot = arr[high]; // Chon pivot la phan tu cuoi
    int i = low - 1;       // Chi so nho hon pivot

    for (int j = low; j < high; j++){
        quickSortComparisons++; // Tang bien dem so sanh
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
    vector<int> arr1 = {5, 2, 9, 1, 5, 6};
    vector<int> arr2 = arr1;
    quickSort(arr1, 0, arr1.size() - 1);
    mergeSort(arr2, 0, arr2.size() - 1);
    cout << "So lan thuc hien so sanh bang Merge Sort: " << mergeSortComparisons << endl;
    cout << "So lan thuc hien so sanh bang Quick Sort: " << quickSortComparisons << endl;
    return 0;
}