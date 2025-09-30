import java.util.Scanner;
public class p08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] INPUT = sc.nextLine().split(" ");

        if (INPUT[0].equals(INPUT[1])){
            System.out.println("0");
        }
        else if (INPUT[0].equals("Y") && INPUT[1].equals("O") ||INPUT[0].equals("O") && INPUT[1].equals("X")||INPUT[0].equals("X") && INPUT[1].equals("Y")){
            System.out.println("2");

        }
        else{
            System.out.println("1");
        }


    }


}
