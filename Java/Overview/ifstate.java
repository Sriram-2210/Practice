package Overview;

public class ifstate {
    public static void main(String[] args) {
        int x = 10, y = 20;
        if(x < y) System.out.println("x is less than y" + "," + " " + "x=" + x + "," + "y="+ y);
        x = x * 2;
        if(x == y) System.out.println("x now equals y" + "," + " " + "x=" + x + ","+ "y=" + y);
        x  = x * 2;
        if(x > y) System.out.println("x now greater than y" + "," + " " + "x=" + x + "," + "y=" + y);
        // This is the indication of commenting a single line in java
    }
    
}
