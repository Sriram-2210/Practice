package DVA;
public class booleantest {
    public static void main(String[] args) {
        boolean a, b, c, d;
        a = true;
        b = false;
        //System.out.println("a is " + a);
        //System.out.println("b is " + b);
        c = a && b;
        d = a || b;
        if(c) System.out.println("c is " + c);
        else System.out.println("c is " + c);
        if (d) System.out.println("d is " + d);
        else System.out.println("d is " + d);
        System.out.println("10 > 9 " + "is" + " " + (10 > 9));
        System.out.println("10 > 11 " + "is" + " " + (10 > 11));
    }
}
