import time
start_time = time.time()

def fiboRecur(n):
   if n <= 1:
       return n
   else:
       return(fiboRecur(n-1) + fiboRecur(n-2))

nterms = int(input("Enter n: "))
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fiboRecur(i))

print("-%s seconds -" % (time.time() - start_time))
# time.sleep(60)