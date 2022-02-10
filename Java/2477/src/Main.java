import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int K;
    private static int area;
    private static int a = 0;
    private static int width;
    private static int height;
    private static int[] dirlst;
    private static int[] lenlst;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        K = Integer.parseInt(br.readLine());
        dirlst = new int[6];
        lenlst = new int[6];
        for (int i = 0; i < 6; i++) {
            st = new StringTokenizer(br.readLine());
            int dir = Integer.parseInt(st.nextToken());
            int len = Integer.parseInt(st.nextToken());
            dirlst[i] = dir;
            lenlst[i] = len;
            if (dir == 1 || dir == 2) {
                width = Math.max(width, len);
            } else {
                height = Math.max(height, len);
            }
        }
        area = width * height;

        // 움푹 파인 부분부터 출발
        if (dirlst[0] == 2 && dirlst[5] == 3|| dirlst[0] == 3 && dirlst[5] == 1 ||
                dirlst[0] == 1 && dirlst[5] == 4 || dirlst[0] == 4 && dirlst[5] == 2) {
            a = lenlst[0] * lenlst[5];
        }else{
            for (int i = 0; i < 5; i++) {
                int cur = dirlst[i];
                int next = dirlst[i + 1];
                if (cur == 3 && next == 2|| cur == 1 && next == 3 ||
                        cur == 4 && next == 1 || cur == 2 && next == 4){
                    a = lenlst[i] * lenlst[i + 1];
                    break;
                }
            }
        }

        int res = (area - a) * K;
        System.out.println(res);
    }
}
