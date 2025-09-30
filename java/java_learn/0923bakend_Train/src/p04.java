import java.util.Scanner;
public class p04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ans = sc.nextInt();
        int t = 0;
        while(true){
            int ansi = sc.nextInt();
            if (ans!=ansi){
                t+=1;

            }
            else{
                break;
            }

        }
        System.out.println(t+1);
    }

}



