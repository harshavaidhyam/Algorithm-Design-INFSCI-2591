#quiz 12
#Shriharsha



minmax = [0,0]
i = 2;
def findSmallAndLarge(arr,n):


    if(n % 2 == 0):
        if (arr[0] > arr[1]):
            minmax[0] = arr[0]
            minmax[1] = arr[1]
        else:
            minmax[0] = arr[0]
            minmax[1] = arr[1]
    else:
        minmax[0] = arr[0]
        minmax[1] = arr[0]

        i = 1


        while (i < n - 1):
            if (arr[i] > arr[i + 1]):
                if (arr[i] > minmax[1]):
                    minmax[1] = arr[i]

                if (arr[i + 1] < minmax[0]):
                    minmax[0] = arr[i + 1]
            else:
                if (arr[i + 1] > minmax[1]):
                    minmax[1] = arr[i + 1]

                if (arr[i] < minmax[0]):
                    minmax[0] = arr[i]


            i += 2




#test case 1
print(" ")
print("test case 1: ")
arr1 = [ 1, 8, 3, 9, 6, 5, 4]
N = len(arr1)


findSmallAndLarge(arr1, N);
print( "Smallest is: " , minmax[0] )
print( "Largest is: " , minmax[1] )
print(" ")


#test case 2

print("test case 2: ")
arr2 = [ 9, 8, 7, 6, 10]
N = len(arr2)


findSmallAndLarge(arr2, N);
print( "Smallest is: " , minmax[0] )
print( "Largest is: " , minmax[1] )
print(" ")

#test case 3

print("test case 3: ")
arr3 = [ 11, 2, 3, 4, 5, 7, 8, 9, 10]
N = len(arr3)


findSmallAndLarge(arr3, N);
print( "Smallest is: " , minmax[0] )
print( "Largest is: " , minmax[1] )



