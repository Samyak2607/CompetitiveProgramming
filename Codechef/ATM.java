import java.util.*;

class sol{
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        double w=sc.nextDouble();
        double amt=sc.nextDouble();
        if(w%5==0 && (w+0.5)<=amt){
            amt=amt-w-0.5;
        }
            System.out.printf("%.2f",amt);
    }
}
