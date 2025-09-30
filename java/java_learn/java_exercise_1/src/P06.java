import java.util.Scanner;


public class P06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n >=1000) {
            System.out.println(n*=0.11);
        }
        else{
            System.out.println(0);
        }
    }
}
