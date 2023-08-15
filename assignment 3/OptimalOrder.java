import java.io.*;
import java.util.*;
import java.time.LocalDate;
import java.lang.*;

public class OptimalOrder
{

    static char name;


    static void OrderPara(int i, int j, int n, int[][] bracket)
    {

        if (i == j)
        {
            System.out.print(name++);
            return;
        }

        System.out.print('(');


        OrderPara(i, bracket[j][i], n, bracket);


        OrderPara(bracket[j][i] + 1, j, n, bracket);

        System.out.print(')');
    }

    static void matrixChainOrder(int[] p, int n)
    {


        int[][] m = new int[n][n];

        for (int L = 2; L < n; L++)
        {
            for (int i = 1; i < n - L + 1; i++)
            {
                int j = i + L - 1;
                m[i][j] = Integer.MAX_VALUE;
                for (int k = i; k <= j - 1; k++)
                {

                    int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                    if (q < m[i][j])
                    {
                        m[i][j] = q;

                        m[j][i] = k;
                    }
                }
            }
        }


        name = 'A';

        System.out.print("Optimal Parenthesization is: ");
        OrderPara(1, n - 1, n, m);
       
    }

    public static void main(String[] args)
    {
        long start=0;
        long end=0;
        start=System.nanoTime();
        end= System.nanoTime();
        int[] arr = { 1,2};
        int n = arr.length;
        matrixChainOrder(arr, n);
        System.out.println("\n Total time is"+(end-start));
    }
}

