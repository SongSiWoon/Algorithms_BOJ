import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        str = str.toUpperCase();
        System.out.println(sol(str));
    }

    public static char sol(String str) {
        int[] alpha = new int[26];
        for (int i = 0; i < str.length(); i++) {
            int idx = str.charAt(i) - 'A';
            alpha[idx] = alpha[idx] + 1;
        }
        int MAX = -1;
        char res = ' ';
        for (int i = 0; i < 26; i++) {
            if (MAX < alpha[i]) {
                MAX = alpha[i];
                res = (char) (i + 65);
            } else if (MAX == alpha[i]) {
                res = '?';
            }
        }
        return res;
    }
}
