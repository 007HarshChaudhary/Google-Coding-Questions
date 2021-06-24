# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:22:23 2020

@author: Harsh Chaudhary
"""


# FOOBAR Level 5 - Dodge the Lasers
#
# Oh no! You've managed to escape Commander Lambdas collapsing space station in
# an escape pod with the rescued bunny prisoners - but Commander Lambda isnt
# about to let you get away that easily. She's sent her elite fighter pilot
# squadron after you - and they've opened fire!
#
# Fortunately, you know something important about the ships trying to shoot you
# down. Back when you were still Commander Lambdas assistant, she asked you to
# help program the aiming mechanisms for the starfighters. They undergo
# rigorous testing procedures, but you were still able to slip in a subtle bug.
# The software works as a time step simulation: if it is tracking a target that
# is accelerating away at 45 degrees, the software will consider the targets
# acceleration to be equal to the square root of 2, adding the calculated
# result to the targets end velocity at each timestep. However, thanks to your
# bug, instead of storing the result with proper precision, it will be
# truncated to an integer before adding the new velocity to your current
# position.  This means that instead of having your correct position, the
# targeting software will erringly report your position as
# sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas
# testing, but enough that it might just save your life.
#
# If you can quickly calculate the target of the starfighters' laser beams to
# know how far off they'll be, you can trick them into shooting an asteroid,
# releasing dust, and concealing the rest of your escape.  Write a function
# answer(str_n) which, given the string representation of an integer n, returns
# the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as
# a string. That is, for every number i in the range 1 to n, it adds up all of
# the integer portions of i*sqrt(2).
#
# For example, if str_n was "5", the answer would be calculated as
# floor(1*sqrt(2)) +
# floor(2*sqrt(2)) +
# floor(3*sqrt(2)) +
# floor(4*sqrt(2)) +
# floor(5*sqrt(2))
# = 1+2+4+5+7 = 19
# so the function would return "19".
#
# str_n will be a positive integer between 1 and 10^100, inclusive. Since n can
# be very large (up to 101 digits!), using just sqrt(2) and a loop won't work.
# Sometimes, it's easier to take a step back and concentrate not on what you
# have in front of you, but on what you don't.
 
# This particular problem is heavy on the mathematics, but it really is
# brilliant.
#
# This problem is an example of a Beatty sequence. For a positive irrational
# number r, the Beatty sequence is as follows: floor(r), floor(2r), etc. If
# r > 1 (which in this case it is: sqrt(2) > 1), then s = r / (r - 1). These
# two numbers satisfy 1 / r + 1 / s = 1. s also generates its own Beatty
# sequence: floor(s), floor(2s), etc. And there is a nice property associated
# with these sequences - they partition the natural numbers. Meaning that
# together, the sequences are the natural numbers.
#
# Now that we have that, let m = floor(n * r) (n = int(str_n)). Then the sum of
# the Beatty sequence produced by r up to m (S(r, n)) and the Beatty sequence
# produced by s up to m (S(s, floor(m / s))) is m(m + 1) / 2. Now, we can do
# some fancy math with the floor and ceiling functions:
#
#   floor(m / s)    = floor(m(1 - 1 / r))       -- 1 / r + 1 / s = 1
#                   = floor(m - m / r)
#                   = m - ceil(m / r)           -- Relationship between ceiling
#                                               -- and floor functions
#
# Let's take a detour here for a minute to derive something:
#
# rn - 1 < m = floor(rn) < rn
# n - 1 / r < floor(rn) / r < n
# n <= ceil(floor(rn) / r) = ceil(m / r) <= n
#
# So:
#
#   floor(m / s)    = m - ceil(m / r)
#                   = m - n
#                   = floor(rn) - n
#                   = floor(rn - n)
#                   = floor(n(r - 1))
#
# We'll call the final value n'. Using the property that the sum of S(r, n) and
# S(s, floor(m / s)) is m(m + 1) / 2,
#
# S(r, n)   = m(m + 1) / 2 - S(s, n')
#           = (n' + n) (n' + n + 1) / 2 - S(s, n')
# S(sqrt(2), n) = (n' + n) (n' + n + 1) / 2 - S(2 + sqrt(2), n')
#
# Using special sums, we obtain the following:
# S(sqrt(2), n) = (n' + n) (n' + n + 1) / 2 - n'(n' + 1) - S(sqrt(2), n')
#
# The following code basically implements the equation. However, there is one
# final caveat. Using sqrt(2) explicitly in the code will not give you the
# correct answer. Why? Precision issues. Floating point numbers are stored
# using only a limited number of bits in Python. However, Python can store
# arbitrarily large integers. So the fix? Store sqrt(2) as a very, very big
# integer. Convert as necessary.
 
'''
# Store sqrt(2) as a very big int
SQRT2MINUS1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
 
def recurse(n):

 
    if n == 0:
        return 0
    else:
 
    # Calculate n'
    n_prime = str(int(n) * SQRT2MINUS1)
 
    # Account for the fact that we are using an integer representation of
    # sqrt(2), a float
    if len(n_prime) > len(str(SQRT2MINUS1)):
       n_prime = int(n_prime[:len(n_prime) - len(str(SQRT2MINUS1))])
    else:
       n_prime = 0
 
    # The recursion derived above
    return (n_prime + n) * (n_prime + n + 1) / 2 - n_prime * (n_prime + 1) - recurse(n_prime)
 
 
def answer(n):
    return recurse(int(n)
        
D = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
def sol(num):
    if num==1: return 1
    if num<1: return 0
    N = (D*num)//(10**100)
    return ((num*N) + num*(num+1)//2 - N*(N+1)//2 - sol(N))

def solution(s):
    return str(sol(long(n)))

'''
from decimal import Decimal, getcontext
getcontext().prec = 101
D = Decimal(2).sqrt() - 1

def solution(s):
    n = long(s)
    return str(sol(n))

def sol(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    N = long(D * n)
    return n*N + n*(n + 1)//2 - N*(N + 1)//2 - sol(N)