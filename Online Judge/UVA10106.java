import java.util.Scanner;
import java.math.BigInteger;

class Main{
    public static void main(String [] args){
        String a,b;
        Scanner in = new Scanner(System.in);
        while((a = in.nextLine())!= null && !a.equals("")){
            b = in.nextLine();
            BigInteger a2 = new BigInteger(a);
            BigInteger b2 = new BigInteger(b);
            System.out.println(a2.multiply(b2));
        }
    }
}