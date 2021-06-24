

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count=0
    sorted_arr = sorted(arr)
    visited = [False for _ in range(len(arr)+1)]

    ans = 0

    for i in range(len(arr)-1):
        if not visited[arr[i]]:
            visited[arr[i]] = True
        
            count = 0
            pos = arr[i]-1
            while not visited[arr[pos]]:
                visited[arr[pos]] = True
                pos = arr[pos]-1
                count += 1
        
            ans += count   
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
