# 1 - (0, 0.16y)  n - 50 , 1,000 , 50,000 , 1,00,000
# 2 - ( 0.85x - 0.04y , -0.04x+0.85y+1.6)
# 3 - (0.2x - 0.26y , 0.23x+0.22y+1.6)
# 4 - ( -0.15x + 0.28y, 0.26x+0.24y+0.44)
import random
import matplotlib.pyplot as plt
def dice_throw(c , a,  b):
    sum = 0
    if(c == 1):
        sum = 0.0*a
    if(c == 2):
        sum = 0.85*a-0.04*b
    if(c == 3):
        sum = 0.2*a-0.26*b
    if(c == 4):
        sum = -0.15*a+0.28*b
    return sum
def dice_throw2(c , a,  b):
    sum = 0
    if(c == 1):
        sum = 0.16*b
    if(c == 2):
        sum = 0.04*a+0.85*b+1.6
    if(c == 3):
        sum = 0.23*a+0.22*b+1.6
    if(c == 4):
        sum = 0.26*a+0.24*b+0.44
    return sum
x=[0]
y=[0]
n = input("Enter the Range")
n = int(n)
for i in range(n):
    a = (x[-1])
    #print("a=",a)
    b = (y[-1])
    #print("b=",b)
    c = random.randint(1,4)
    #print("c=",c)
    x.append(dice_throw(c , a , b))
    y.append(dice_throw2(c , a , b))
# plotting the points
plt.scatter(x, y, label= "dots", color= "green",
            marker= ".", s=5)

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()
#print (x)
#print (y)
