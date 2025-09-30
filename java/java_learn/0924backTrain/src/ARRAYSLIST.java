import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
public class ARRAYSLIST {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>();
        A.add(1);
        A.add(2);
        A.add(3);
        System.out.println(A.get(0));
        A.set(0,4);
        System.out.println(A.get(0));
        A.remove(0);
        System.out.println(A);
        A.add(0,99);
        System.out.println(A);
        Collections.sort(A);
        System.out.println(A);
    }
}
