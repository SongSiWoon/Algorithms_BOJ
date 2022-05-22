import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int INF = 987654321;
    private static int[][] graph;
    private static int[][] dp;
    private static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        dp = new int[n][(1 << n) - 1];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], INF);
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j <n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(tsp(0, 1));

    }

    public static int tsp(int cur, int check) {
        if (check == (1 << n) - 1) {
            if (graph[cur][0] == 0) {
                return INF;
            }
            return graph[cur][0];
        }

        if (dp[cur][check] != INF) {
            return dp[cur][check];
        }

        for (int i = 0; i < n; i++) {
            int next = check | (1 << i);
            if ((check & (1 << i)) == 0 && graph[cur][i] != 0) {
                dp[cur][check] = Math.min(dp[cur][check], tsp(i, next) + graph[cur][i]);
            }

        }
        return dp[cur][check];
    }
}
