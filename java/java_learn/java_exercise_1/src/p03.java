import java.util.*;
public class p03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char a,b,c;
        a=sc.nextLine().charAt(0);
        b=sc.nextLine().charAt(0);
        c=sc.nextLine().charAt(0);
        char[] list = {a, b, c};
        char max=0;
        for(char i : list){
        if(i>=max){
            max=i;
        }

    }
    System.out.println(max);
    }
}




