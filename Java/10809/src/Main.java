import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        String str = sc.next();
        int[] res = new int[26];
        Arrays.fill(res, -1);

        for (int i = 0; i < str.length(); i++) {
            int idx = str.charAt(i) - 'a';
            if (res[idx] == -1) {
                res[idx] = i;
            }
        }
        for (int i : res) {
            sb.append(i).append(" ");
        }
        System.out.println(sb);

    }
}
