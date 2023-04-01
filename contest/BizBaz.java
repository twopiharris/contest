import java.util.*;
import java.io.*;

public class BizBaz{
    public static void main(String[] args){
        new BizBaz();
    }
    
    public BizBaz(){
        try {
            int[] primes = {2, 3, 5, 7, 11, 13};
            String[] terms = {"Biz", "Baz", "Buzz", "Boz", "Beez", "Bizzle"};
            
            File inFile = new File("bizBazIn.txt");
            Scanner input = new Scanner(inFile);
            
            while (input.hasNext()){
                int attack = input.nextInt();
                boolean hit = true;
                System.out.print(attack + " ");
                for (int i = 0; i < 6; i++){
                    int prime = primes[i];
                    if ((attack % prime) == 0){
                        hit = false;
                        System.out.print(terms[i] + " ");
                    } // end if
                } // end for
                
                if (hit){
                    System.out.print("Bummer");                    
                }// end if
                System.out.println();
            } // end while
            //inFile.close();
        } catch (IOException e){
            System.out.println(e.getMessage());
        } // end try
    } // end constructor
    
} // end class def
