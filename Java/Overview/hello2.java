package Overview;

public class hello2 {
    public static void main(String[] args) {
        int num = 100;
        System.out.println("This is num:"+ num);
        num = num *2;
        System.out.println(" The value of num now is: " + num);
    }
    
}

/* Here in the line 5, the plus sign causes the value of num to be appended to the string and 
 * the resulting string is treated as output. Actually, first the num is converted from integer 
 * to string and then concatenated. This approach is generalized. 
 * Note: In upcoming, more detalis will be understood. 
 */
