package EigenValuesAndEigenVectos;

import Matrices.Determinant;
import java.util.Random;

public class EigenValues {
    public static void main(String[] args) {
        int n = 3;
        int[][] mat = new int[3][3];
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mat[i][j] = rand.nextInt(10);
            }
        }
        Determinant D = new Determinant();
        int det = D.determinant(mat, n);
        int trace = 0;
        for (int i = 0; i < n; i++) {
            trace += mat[i][i];
        }
        int minor_sum =minorSum(mat, n);
       

        System.out.println("Determinant = " + minor_sum);

    }
    public static int minorSum(int[][] mat, int n) {
    int sum = 0;

    for (int j = 0; j < n; j++) {
        int[][] minor = new int[n - 1][n - 1];
        int rowIndex = 0;
        for (int row = 1; row < n; row++) { // skip first row
            int colIndex = 0;
            for (int col = 0; col < n; col++) {
                if (col == j) continue; // skip column j
                minor[rowIndex][colIndex++] = mat[row][col];
            }
            rowIndex++;
        }
        sum += D.determinant(minor, n - 1); // D is your determinant class
    }

    return sum;
}

}
