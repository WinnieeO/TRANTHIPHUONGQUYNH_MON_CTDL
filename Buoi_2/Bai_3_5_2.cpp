#include <iostream>
#include <vector>
#include <time.h>
#include <cstdlib>
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

// Ham tao mang ngau nhien
vector<int> generateRandomArray(int size) {
    vector<int> arr(size);
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100;
    }
    return arr;
}

int main(){
    srand(static_cast<unsigned>(time(0)));

    // Mang 5000 phan tu
    vector<int> arr5000 = generateRandomArray(5000);
    vector<int> arr1 = arr5000;
    vector<int> arr2 = arr5000;

    clock_t begin1 = clock();
    bubbleSort(arr1);
    clock_t end1 = clock();

    clock_t begin2 = clock();
    mergeSort(arr2, 0, arr2.size() - 1);
    clock_t end2 = clock();

    cout << "Thoi gian chay cua Bubble Sort voi mang 5000 phan tu: " << (float)(end1 - begin1) / CLOCKS_PER_SEC << "s" << endl;
    cout << "Thoi gian chay cua Merge Sort voi mang 5000 phan tu: " << (float)(end2 - begin2) / CLOCKS_PER_SEC << "s" << endl << endl;

    // Mang 10000 phan tu
    vector<int> arr10000 = generateRandomArray(10000);
    arr1 = arr10000;
    arr2 = arr10000;

    clock_t begin3 = clock();
    bubbleSort(arr2);
    clock_t end3 = clock();
    
    clock_t begin4 = clock();
    mergeSort(arr1, 0, arr1.size() - 1);
    clock_t end4 = clock();

    cout << "Thoi gian chay cua Bubble Sort voi mang 10000 phan tu: " << (float)(end3 - begin3) / CLOCKS_PER_SEC << "s" << endl;
    cout << "Thoi gian chay cua Merge Sort voi mang 10000 phan tu: " << (float)(end4 - begin4) / CLOCKS_PER_SEC << "s" << endl << endl;

    // Mang 20000 phan tu
    vector<int> arr20000 = generateRandomArray(20000);
    arr1 = arr20000;
    arr2 = arr20000;

    clock_t begin5 = clock();
    bubbleSort(arr1);
    clock_t end5 = clock();

    clock_t begin6 = clock();
    mergeSort(arr2, 0, arr2.size() - 1);
    clock_t end6 = clock();

    cout << "Thoi gian chay cua Bubble Sort voi mang 20000 phan tu: " << (float)(end5 - begin5) / CLOCKS_PER_SEC << "s" << endl;
    cout << "Thoi gian chay cua Merge Sort voi mang 20000 phan tu: " << (float)(end6 - begin6) / CLOCKS_PER_SEC << "s" << endl;

    return 0;
}