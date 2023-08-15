
import sys
from datetime import datetime
start_time = datetime.now()

def matrixChainMultiplication(prem, i, j):
 
    # base case: 1 matrix
    if j <= i + 1:
        return 0
 
  
    min = sys.maxsize
 
 
    for k in range(i + 1, j):
 
    
        cost = matrixChainMultiplication(prem, i, k)
 
        cost += matrixChainMultiplication(prem, k, j)
 
        cost += prem[i] * prem[k] * prem[j]
 
        if cost < min:
            min = cost
 
    return min
 
 
if __name__ == '__main__':
 
   
    prem = [76,84,273,77,666,2904,984,974,83]
 
    print(' Minimum cost is', matrixChainMultiplication(prem, 0, len(prem) - 1))


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))