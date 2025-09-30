import java.util.Scanner;

public class p02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n%4==0&&n%100!=0||n%100==0&&n%400==0){
            System.out.println("閏年");
        }
        else{
            System.out.println("平年");
        }




    }
}
