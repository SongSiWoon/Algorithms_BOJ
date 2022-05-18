import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static class Item {
        private int weight;
        private int value;

        public Item(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        Item[] items = new Item[n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            items[i] = new Item(w, v);
        }
        System.out.println(knapsack(items, n, k));

    }

    private static int knapsack(Item[] items, int n, int w) {
        int[][] dp = new int[n + 1][w + 1];
        for (int i = 0; i < w; i++) {
            dp[0][i] = 0;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= w; j++) {
                if (items[i].weight > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(items[i].value + dp[i - 1][j - items[i].weight], dp[i - 1][j]);
                }
            }

        }
        return dp[n][w];
    }
}
