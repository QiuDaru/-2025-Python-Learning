import java.util.Scanner;

public class p07
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = n/60;
        int b = n%60;
        System.out.printf("%02d:%02d",a,b);
    }
}
