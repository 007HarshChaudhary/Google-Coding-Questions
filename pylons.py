# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:54:45 2020

@author: Harsh Chaudhary
"""

for t_itr in range(int(input())):
    R, C = list(map(int, input().split()))
    arr = [[False for c in range(C)] for r in range(R)]
    output = [[R//2, C//2]]
    arr[R//2][C//2] = True
    LIMIT = R*C
    count=1
    r_last, c_last = output[-1]
    previous_iteration_made_change = True
    
    while previous_iteration_made_change:
        
        previous_iteration_made_change = False
        
        for r in range(R):
            for c in range(C):            
                
                if arr[r][c]==False and r_last!=r and c_last!=c and r_last-c_last!=r-c and r_last+c_last!=r+c:
                    arr[r][c] = True
                    r_last = r
                    c_last = c
                    output.append([r, c])
                    count+=1
                    previous_iteration_made_change = True
    if count!=LIMIT:
        print('Case #{}: IMPOSSIBLE'.format(t_itr+1))
    elif count==LIMIT:
        print('Case #{}: POSSIBLE'.format(t_itr+1))
        for v in output:
            print(v[0]+1, v[1]+1)
###############################################################################################################
            ###################################################################################################
###############################################################################################################
from itertools import product, repeat
from random import choice


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        R, C = map(int, input().split())  # the numbers of rows and columns

        if R < 2 or C < 2 or R + C < 7:
            print('Case #{}: IMPOSSIBLE'.format(case))
        else:
            print('Case #{}: POSSIBLE'.format(case))

            while True:
                grid = [[False]*C for _ in repeat(None, R)]
                moves = []
                last = None
                for _ in repeat(None, R*C):
                    candidates = ([(r, c) for r, c in product(range(R), range(C)) if not grid[r][c]
                                   and r != last[0] and c != last[1] and last[0] - last[1] != r - c
                                   and last[0] + last[1] != r + c]
                                  if last is not None else list(product(range(R), range(C))))
                    if not candidates:
                        break
                    cell = choice(candidates)
                    moves.append(cell)
                    grid[cell[0]][cell[1]] = True
                    last = cell
                else:
                    for r, c in moves:
                        print(r+1, c+1)
                    break


main()
