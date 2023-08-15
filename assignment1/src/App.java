

import java.util.*;
 
class GFG {
 

    public static int Minm(int arr[], int i,
                                 int sumCalculated,
                                 int sumTotal)
    {

        if (i == 0)
            return Math.abs((sumTotal - sumCalculated)
                            - sumCalculated);
 

        return Math.min(
            Minm(arr, i - 1,
                       sumCalculated + arr[i - 1],
                       sumTotal),
            Minm(arr, i - 1, sumCalculated,
                       sumTotal));
    }
 

    public static int findMin(int arr[], int n)
    {

        int sumTotal = 0;
        for (int i = 0; i < n; i++)
            sumTotal += arr[i];
 

        return Minm(arr, n, 0, sumTotal);
    }
 

    //test case 1:

    public static void main(String[] args)
    {
        int arr[] = { 10, 20, 15, 5, 25, 100 };
        int n = arr.length;
        System.out.print("Minimum difference"
                         + " between two lists:  "
                         + findMin(arr, n));
                         System.out.print("\n");
    }
}
 


// This code is contributed by the school of computing and information
// Authors- 