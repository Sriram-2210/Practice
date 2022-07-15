package DVA;
public class character {
    public static void main(String[] args) {
        char c1, c2, c3;
        c1 = 'Y';
        c2 = '9';
        c3 = 90;
        System.out.println("The value of " + c1 + "is" + " " + c2);
        System.out.println(" Char 1 and Char 3 are ");
        System.out.print(c1 + " " + c3);
    }
}

/* 
Here c2 = '9' considers the interger 9 as a singe character and thus appends in the 
first print statement. But c3 = 90 considers the ascii value of 90 as Z and thus it gets appened.
Ascii ranges from 0 to 127.
*/