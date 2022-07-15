package DVA;

public class scope {
    public static void main(String[] args) {
        int x =10;
        if(x%2==0){
            int y = 20;
            x = x * y;
            System.out.println(x);
        }
        // here y exists in the if conditional block and thus from here it's out of scope
        // Where as x is defined globally thus it can be called here as well.
    }
}
