// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Random;
class inverse_of_2by2 {
    public static void main(String[] args) {
        int [][] arr =new int [2][2];
        Random rand = new Random();
        for (int i = 0; i <2; i++) {
           for (int j = 0; j <2; j++) {
              arr[i][j] = rand.nextInt(10);
           }
        }
         for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                System.out.print(arr[i][j]+" ");
                
            }
            System.out.println();
        }
        float denominator =  arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0];
        int tmp = arr[0][0];
        arr[0][0] = arr[1][1];
        arr[1][1]=tmp;
        arr[0][1] = -arr[0][1];
        arr[1][0] = -arr[1][0];
       
        double res[][] = new double[2][2];
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                res[i][j]=arr[i][j]/denominator;
            }
        }
         for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                System.out.print(res[i][j]+" ");
                
            }
            System.out.println();
        }
        
        
        
        
        
    }
}