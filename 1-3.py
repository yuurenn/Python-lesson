# a="AEIKMNORUW"
# print("%s"%(a))
# for b1 in a:
#     for b2 in a:
#         for b3 in a:
#             for b4 in a:
#                 for b5 in a:
#                     for b6 in a:
#                         if b1!=b2!=b3!=b4!=b5!=b6:
#                             print("%s%s%s%s%s%s%s%s"%(b1,b2,b3,b2,b4,b5,b6,b2))
from math import gcd, lcm
from operator import mod

# 5,4,5, 5*6^2+4*6+5
p=5*(6**2)+4*6+5
print(p)
a=p**43
print(a)
a=a%493
# a=a%8
print(a)

########関数部分##############
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
############################
 
 
#####関数をつかってみる．#####
######今回は二進数に変換######
x10 = a
x2 = Base_10_to_n(x10, 6)
print( x2 )#"100011"が表示される．


# """nを素因数分解"""
# """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         print(i)
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])

#     if temp!=1:
#         arr.append([temp, 1])

#     if arr==[]:
#         arr.append([n, 1])

#     return arr

# print(factorization(114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541) )

# ## [[2, 3], [3, 1]] 
# ##  24 = 2^3 * 3^1
# def prime_factorize(n):
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a

# print(prime_factorize(114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541) )
# print(prime_factorize(2147483647))
# print(lcm(21,53))
# print(mod(17255,44556))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

a=prime_factorize(493)
print(a)
print(lcm(16,28))
"""うにゃ"""