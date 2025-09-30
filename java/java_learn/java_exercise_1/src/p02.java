import java.util.Scanner;
public class p02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a,b,c ;
        a = sc.nextInt();

        b = sc.nextInt();

        c = sc.nextInt();

        System.out.println(Math.max(a,Math.max(b,c)));

    }
}
