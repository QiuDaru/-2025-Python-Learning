import java.util.Scanner;

public class p10_h3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int j = 1; j <= n; j++) {
            //線
            for (int i = n-j; i >= 0; i--) {
                System.out.print("_");
            }
            //優先字
            for (int i = 1; i <= j; i++) {
                System.out.print(i);
            }
            //後字
            for (int i = j - 1; i >= 1; i--) {
                System.out.print(i);
            }
            //後線
            for (int i = n-j; i >= 0; i--) {
                System.out.print("_");
            }
            System.out.println();
        }
    }
}
