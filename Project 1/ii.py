import time
start_time = time.time()
def fiboiter(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print(end=' ')
        print('0',a,b,end=' ')
        for i in range(n-3):
            sum = a + b
            b=a
            a= sum
            print(sum,end=' ')
        print()
        return b
         
fiboiter(42)

print("- %s seconds -" % (time.time() - start_time))