import java.util.Arrays;
import java.util.Collections;
public class ARRAY {
    public static void main(String[] args) {
        Integer[] A = new Integer[4];
        A[0] = 1;
        A[1] = 2;
        A[2] = 3;
        A[3] = 4;
        System.out.println(Arrays.toString(A));
        System.out.println(A.length);
        System.out.println(A[0]);
        A[0] = 10;
        System.out.println(Arrays.toString(A));
        Arrays.sort(A);//小到大
        System.out.println(Arrays.toString(A));
        Arrays.sort(A,Collections.reverseOrder());
        System.out.println(Arrays.toString(A));
    }
}
