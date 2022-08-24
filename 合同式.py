# ax≡1(mod N)
# ax-1≡0(mod N)
# aとNの最大公約数を求める
from math import gcd
from operator import mod

# import numpy as np

a=171
n=287
print(str(a)+"x≡1(mod"+str(n)+")")
d=gcd(a,n)
if d==1:
    for num in range(n):
        if (a*num)%n==1:
            break
    print("x≡"+str(num)+"(mod"+str(n)+")")

else:
    print("解なし")

a=19814**17255
print(mod(a,89711))