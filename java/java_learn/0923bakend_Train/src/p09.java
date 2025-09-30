import java.util.Scanner;
public class p09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        for(int i=1;i<=t;i++){
        String[] n = sc.nextLine().split(":");
        int n1 = Integer.parseInt(n[0]);
        int n2 = Integer.parseInt(n[1]);
        if(n1>=5&& n1<=9 ||n1==10&&n2<30){
            System.out.println("Y");

        }
        else{
            System.out.println("N");
        }}

    }
}
