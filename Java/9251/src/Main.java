import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String strX = br.readLine();
        String strY = br.readLine();
        System.out.println(LCS(strX, strY));

    }

    public static int LCS(String strX, String strY) {
        int lenX = strX.length();
        int lenY = strY.length();
        int[][] dp = new int[lenX + 1][lenY + 1];

        for (int i = 1; i <= lenX; i++) {
            for (int j = 1; j <= lenY; j++) {
                if (strX.charAt(i - 1) == strY.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[lenX][lenY];
    }
}
