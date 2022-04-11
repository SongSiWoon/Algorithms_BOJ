import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }
        //System.out.println(Arrays.toString(nums));
        //Selection(nums, n);
        //Insertion(nums, n);
        //Bubble(nums, n);
        MergeSort(nums, 0, n - 1);
        //System.out.println(Arrays.toString(nums));
        System.out.println(Arrays.stream(nums).mapToObj(String::valueOf).collect(Collectors.joining("\n")));
    }

    public static void Selection(int[] arr, int size) {
        for (int i = 0; i < size - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < size; j++) {
                if (arr[minIdx] > arr[j]) {
                    minIdx = j;
                }
            }
            swap(arr, minIdx, i);
        }
    }

    public static void Insertion(int[] arr, int size) {
        for (int i = 1; i < size; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && key < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    public static void Bubble(int[] arr, int size) {
        for (int i = 0; i < size - 1; i++) {
            for (int j = 1; j < size - i; j++) {
                if (arr[j - 1] > arr[j]) {
                    swap(arr, j - 1, j);
                }
            }
        }
    }

    public static void MergeSort(int[] arr, int start, int end) {
        int mid = (start + end) / 2;
        if (start < end) {
            MergeSort(arr, start, mid);
            MergeSort(arr, mid + 1, end);
            Merge(arr, start, end);
        }
    }

    public static void Merge(int[] arr, int start, int end) {
        int mid = (start + end) / 2;
        int[] Left = Arrays.copyOfRange(arr, start, mid + 1);
        int[] Right = Arrays.copyOfRange(arr, mid + 1, end + 1);
        int l = 0, r =  0, idx = start;
        while (l < Left.length && r < Right.length) {
            if (Left[l] <= Right[r]) {
                arr[idx] = Left[l];
                l++;
            } else {
                arr[idx] = Right[r];
                r++;
            }
            idx++;
        }

        while (l < Left.length) {
            arr[idx] = Left[l];
            l++;
            idx++;
        }
        while (r < Right.length) {
            arr[idx] = Right[r];
            r++;
            idx++;
        }

    }

    public static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}
