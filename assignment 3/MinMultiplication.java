
import java.io.*;
import java.util.*;
import java.time.LocalDate;
import java.lang.*;
public class MinMultiplication
{

    static int[][] dp = new int[100][100];


    static int matrixMultMin(int[] p, int i, int j)
    {
        if (i == j)
        {
            return 0;
        }
        if (dp[i][j] != -1)
        {
            return dp[i][j];
        }
        dp[i][j] = Integer.MAX_VALUE;
        for (int k = i; k < j; k++)
        {
            dp[i][j] = Math.min(
                    dp[i][j], matrixMultMin(p, i, k)
                            + matrixMultMin(p, k + 1, j)
                            + p[i - 1] * p[k] * p[j]);
        }
        return dp[i][j];
    }

    public static int MatrixChainOrder(int[] p, int n)
    {
        int i = 1, j = n - 1;
        return matrixMultMin(p, i, j);
    }

    // Driver Code
    public static void main (String[] args)
    {


        long start=0;
        long end=0;
        int w=0;

        int arr[] = { 1,2,3,4,5,10,20,30,34, 354, 567, 987, 636 ,678,789,799};
        int n= arr.length;
        start=System.nanoTime();
        end=System.nanoTime();
        for (int[] row : dp)
            Arrays.fill(row, -1);

        System.out.println("n = "+n+" and time taken in nanoseconds is "+(end-start));
    }
}