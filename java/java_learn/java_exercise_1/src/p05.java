import java.util.Scanner;

public class p05 {
    public static void main(String[] args) {
        int a,b;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        if(a-b<0){
            System.out.println((a-b)*-1);

        }
        else{
            System.out.println(a-b);
        }



    }
}

