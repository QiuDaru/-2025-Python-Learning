import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        for (int i=0; i<n;i+=1){
            String name = input.nextLine();
            System.out.println(name+" Chan Hai~ ");
        }
    }
}
