import sys
import os

# For using functions from assignment_1 to test in test_assignment_1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.main.assignment_2 import *

print("Problem 1: Neville's Method")
Nev_x = [3.6,3.8,3.9]
Nev_y = [1.675,1.436,1.318]

result = Neville(Nev_x,Nev_y,3.7)
print(result)
print("\n")

print("Problem 2: Newton's Forward")
NF_x = [7.2,7.4,7.5,7.6]
NF_y = [23.5492,25.3913,26.8224,27.4589]

NewtonForward(NF_x,NF_y,7.3)
print("\n")

print("Problem 4: Divided Difference")
DD_x = [3.6,3.8,3.9]
f = [1.675,1.436,1.318]
f_prime = [-1.195,-1.188,-1.182]

result3 = DivDiff(DD_x,f,f_prime)

result3
print("\n")

print("Problem 5: Cubic Spline Method")
CS_x = [2,5,8,10]
CS_y = [3,5,7,9]

CubicSpline(CS_x,CS_y)



