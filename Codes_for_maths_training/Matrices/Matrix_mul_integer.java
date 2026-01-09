

import java.util.Random;


public class Matrix_mul_integer {
    //matrix multiplication interger
    public static void main(String[] args) {
        int n1=3;
        int n2 =20;
        int n3 = 50;
        int n4 = 60;
        int n5 = 70;
        int n6 = 80;
        int n7 = 100;
        int n8 = 200;
        int n9 = 300;
        int n10 = 500;
        int n11=600;
        int n12 =700;
        
        
        System.out.println(time_tocal(n1));
        System.out.println(time_tocal(n2));
        System.out.println(time_tocal(n3));
        System.out.println(time_tocal(n4));
        System.out.println(time_tocal(n5));
        System.out.println(time_tocal(n6));
        
        System.out.println(time_tocal(n7));
        
        System.out.println(time_tocal(n8));
        
        System.out.println(time_tocal(n9));
        
        System.out.println(time_tocal(n10));
        
        System.out.println(time_tocal(n11));
            System.out.println(time_tocal(n12)); 
        
       

    }
    public static long time_tocal(int n){
        long startTime = System.currentTimeMillis();
         int [][] arr1 =new int [n][n];
        int [][] arr2 = new int[n][n];
        int [][] res = new int[n][n];
        
       Random rand = new Random();
       for (int i = 0; i < n; i++) {
            for (int j = 0; j <n; j++) {
           arr1[i][j] = rand.nextInt(10);  // random integers 0-9
           arr2[i][j] = rand.nextInt(10);
 
        }
       }
        for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          res[i][j] = 0;
           for (int k = 0; k < n; k++) {
             res[i][j] += arr1[i][k] * arr2[k][j];
            }
    }
}


        long endTime = System.currentTimeMillis();
        long tt = endTime-startTime;
       
        

        return tt;
        
    }
    
    
}