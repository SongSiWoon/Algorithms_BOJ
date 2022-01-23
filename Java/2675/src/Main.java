import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int repeat = Integer.parseInt(st.nextToken());
            String str = st.nextToken();
            sol(repeat, str);
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static void sol(int repeat, String str) {
        for (int i = 0; i < str.length(); i++) {
            for (int j = 0; j < repeat; j++) {
                sb.append(str.charAt(i));
            }
        }
    }
}
