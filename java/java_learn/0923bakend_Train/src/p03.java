import java.util.Scanner;
public class p03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] s =  sc.nextLine().split(",");
        int a = 0;
        int b = 0;
        for(String s1:s){
            b = Integer.parseInt(s1);
            if (b >=60){
                a+=1;

            }

            }
        if (a>=5){
            System.out.println("過關");

        }
        else{
            System.out.println("卡關");
        }
            }

        }



