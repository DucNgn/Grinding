import java.util.Scanner;

public class stringReversed
{
    public static void swap(char[] target, int a, int b) {
        char temp = target[a];
        target[a] = target[b];
        target[b] = temp;
    }

    public static char[] reverseArray(char[] target, int start, int end) {
        //base case
        if (start > end) {
            return target;
        } else {
            swap(target, start, end); 
            return reverseArray(target, start + 1, end - 1);
        }
    }

    public static void main(String[] args) {
        Scanner keyIn = new Scanner(System.in);
        
        System.out.println("Gimme a string");
        String target = keyIn.nextLine();
        char[] charTarget = target.toCharArray();
        
        char[] resultChar = reverseArray(charTarget, 0, charTarget.length - 1);

        String result = new String(resultChar);

        System.out.println(result);
    }

}