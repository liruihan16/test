#一元二次方程
import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if b*b-4*a*c<0 :
    print("wrong")
elif b*b-4*a*c==0 :
    print(-0.5*b/a)
else :
    print((-b+math.sqrt(b*b-4*a*c))/(2*a))
    print((-b-math.sqrt(b*b-4*a*c))/(2*a))
