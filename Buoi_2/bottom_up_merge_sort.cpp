#include <iostream>
#include <vector>
using namespace std;

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

void bottomUpMergeSort(vector<int>& arr){
    int n = arr.size();
    for (int curr_size = 1; curr_size < n; curr_size = 2 * curr_size){
        for (int left_start = 0; left_start < n - 1; left_start += 2 * curr_size){
            int mid = min(left_start + curr_size - 1, n - 1);
            int right_end = min(left_start + 2 * curr_size - 1, n - 1);
            if (mid < right_end){
                merge(arr, left_start, mid, right_end);
            }
        }
    }
}

int main(){
    vector<int> arr = {5, 2, 9, 1, 5, 6};
    bottomUpMergeSort(arr);

    cout << "Ket qua Merge Sort: ";
    for (int x: arr)
        cout << x << " ";
    cout << endl;
    return 0;
}