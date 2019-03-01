from numpy import double

r=200
circle_num = 0
total_num = 0
oo= (double(r),double(r))
for x in range(0, 64*r+1):
    for y in range(0, 64*r+1):
        distance_square = double(((x/32)-oo[0]))**2 + double(((y/32)-oo[1]))**2
        total_num +=1
        if double(distance_square) < double(r**2):
            circle_num +=1
            pi = 4*(double(circle_num)/total_num)
        print(total_num)
print(pi)
