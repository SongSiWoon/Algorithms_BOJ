import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static class Node {
        private int node;
        private int weight;

        public Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }
    }


    private static List<Node>[] city;
    private static int[] dist;
    private static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        int bus = Integer.parseInt(br.readLine());

        city = new List[n + 1];
        initCity();
        dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        for (int i = 0; i < bus; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            city[s].add(new Node(e, w));
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        dijkstra(start);
        System.out.println(dist[end]);
    }

    public static void initCity() {
        for (int i = 0; i < n + 1; i++) {
            city[i] = new ArrayList<>();
        }
    }

    public static void dijkstra(int start) {
            PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
            pq.add(new Node(start, 0));
            dist[start] = 0;

            while (!pq.isEmpty()) {
                Node curnode = pq.poll();
                int cur = curnode.node;
                int weight = curnode.weight;

                if(weight > dist[cur]){
                    continue;
                }
                for (Node next: city[cur]) {
                    if (dist[next.node] > dist[cur] + next.weight) {
                        dist[next.node] = dist[cur] + next.weight;
                        pq.add(new Node(next.node, dist[next.node]));
                    }
                }
            }
        }
}
