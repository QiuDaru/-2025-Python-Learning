import java.util.Scanner;

public class p10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] INPUT = sc.nextLine().split(" ");

        for(String s: INPUT){
            StringBuilder sb = new StringBuilder(s);
            String ans = sb.reverse().toString();
            System.out.print(ans);
            System.out.print(" ");

        }
}}
