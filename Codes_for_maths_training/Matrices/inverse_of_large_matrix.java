
import java.util.Random;
class inverse_of_large_matrix {
    public static void main(String[] args) {
        int [][] arr1 =new int [3][3];
        Random rand = new Random();
        for (int i = 0; i <3; i++) {
           for (int j = 0; j < 3; j++) {
              arr1[i][j] = rand.nextInt(10);
           }
        }
        int det = determinant(arr1,3);
        if(det<=0) System.out.println("Inverse of the matrix dosen't exist");
        else{
            
        }
    }
    public static int determinant(int [][]arr,int n){
        if(n==1) return arr[0][0];
        if(n==2) return det_square_mat(arr);
        int det = 0;
        for (int j = 0; j < n; j++) {
          int[][] minor = new int[n-1][n-1];
          for (int row = 1; row < n; row++) {
            int colIndex = 0;
            for (int col = 0; col < n; col++) {
               if (col == j) continue;
               minor[row-1][colIndex++] = arr[row][col];
            }
          }
          det += arr[0][j] * ((j % 2 == 0 ? 1 : -1) * determinant(minor,n-1));
        }
      return det;
    }
    public static int det_square_mat(int [][] arr1){
        
      int d = arr1[0][0]*arr1[1][1]-arr1[0][1]*arr1[1][0];
      return d;
        
    }
    
    
}