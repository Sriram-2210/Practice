package DVA;
public class light {
    public static void main(String[] args) {
       int lightspeed;
       long days;
       long seconds;
       long distance;
       //light speed in miles is generally 186000 miles or 3 * 10^8 m/s.
       lightspeed = 186000;
       days = 1000;
       seconds = days * 24 * 60 *60;
       distance = lightspeed * seconds;

       System.out.println("The distance travelled by light in " + days + " days is " + distance + " miles");
    }
    
}
