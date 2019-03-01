import random
import math
from numpy import double

times= int(input("How many times to try? "))
r=200
circle_num = 0
total_num = 0
oo= (double(r),double(r))

i=0
while i < times:
    i += 1
    x= math.fabs(double(random.random()*2*r))
    y= math.fabs(double(random.random()*2*r))
    distance_square = double((x-oo[0]))**2 + double((y-oo[1]))**2
    total_num +=1
    if double(distance_square) < double(r**2):
        circle_num +=1
        pi = 4*(double(circle_num)/total_num)

print(pi)

