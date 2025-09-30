import java.util.Scanner;
public class p05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] n = sc.nextLine().split(":");
        int n1 = Integer.parseInt(n[0]);
        int n2 = Integer.parseInt(n[1]);
        if(n1==8&& n2>=10 || n1>=9&&n1<17||n1==17&&n2<=10){
            System.out.println("at school");

        }
        else{
            System.out.println("off school");
        }

    }
}
