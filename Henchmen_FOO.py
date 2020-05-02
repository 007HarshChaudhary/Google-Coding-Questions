from math import log2
from itertools import accumulate

def solution(total_lambs):
    # Your code here
    A = int(log2(total_lambs+1))
    B = None
    for x_men, total in enumerate(accumulate(fib())):
        if total>total_lambs:
            B =  x_men
            break
    
    print (abs(A-B))

def fib():
    a=1
    b=1
    while True:
        yield a
        a, b = b, a+b


# from math import log2
# from itertools import accumulate


# def answer(lambs):
#     return stingy(lambs) - generous(lambs)


# def generous(lambs):
#     return int(log2(lambs + 1))


# def stingy(lambs):
#     for henchmen, total_pay in enumerate(accumulate(fibonacci())):
#         if total_pay > lambs:
#             return henchmen


# def fibonacci():
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a + b
def stingy(total_lambs):
    """
    Return: the number of henchmen sharing the LAMBs
        if as stingy as possible.
    """
    num = 1
    last = 0
    cur = 1
    total_lambs -= 1
    while total_lambs > 0:
        if total_lambs < last + cur:
            break
        num += 1
        cur, last = cur + last, cur
        total_lambs -= cur

    return num





from math import log

def solution(total_lambs):
    # Your code here
    A = int(log(total_lambs+1, 2))
    B = None

    num = 1
    last = 0
    cur = 1
    total_lambs -= 1
    while total_lambs > 0:
        if total_lambs < last + cur:
            break
        num += 1
        cur, last = cur + last, cur
        total_lambs -= cur
    
    B = num
    answer = abs(A-B)
    print (answer)