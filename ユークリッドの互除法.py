#出力する関数作成したかった

from math import gcd



a_list=[]
b_list=[]
c_list=[]
d_list=[]
print("ユークリッドの互除法をしたい二つの数字を入力")
a=int(input("a:"))
b=int(input("b:"))
# a=155
# b=42
j=a#一次不定方程式で利用
i=0
result = divmod(a, b)
# print(result[0], result[1])
c=int(result[0])
d=int(result[1])
#sequence=[a,b,c,d]
print(str(a)+"="+str(b)+"*"+str(c)+"+"+str(d))
a_list.append(a)
b_list.append(b)
c_list.append(c)
d_list.append(d)
# 繰り返す
while d != 0:
    a=b
    b=d 
    result=divmod(a, b)
    c=int(result[0])
    d=int(result[1])
    print(str(a)+"="+str(b)+"*"+str(c)+"+"+str(d))
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)
    i=i+1
print(a_list)
print(b_list)
print(c_list)
print(d_list)
print(i)
s=i
print("最大公約数",b)
# 一次不定方程式
# i=i-1
# while i!=-1:
#     print(str(d_list[i])+"="+str(a_list[i])+"-"+str(b_list[i])+"*"+str(c_list[i]))
#     i=i-1

i=i-1
# s=s-1
"""ここまでを繰り返す"""
# print(str(d_list[i])+"="+str(a_list[i])+"-"+str(b_list[i])+"*"+str(c_list[i]))
# print(str(d_list[i])+"="+str(a_list[i])+"-("+str(a_list[i-1])+"-"+str(b_list[i-1])+"*"+str(c_list[i-1])+")*"+str(c_list[i]))
# kakeruyatu=c_list[i-1]*c_list[i]+1
# print(str(d_list[i])+"="+str(a_list[i])+"*"+str(kakeruyatu)+"-"+str(a_list[i-1])+"*"+str(c_list[i]))
# print(str(d_list[i])+"=("+str(a_list[i-2])+"-"+str(a_list[i-1])+"*"+str(c_list[i-2])+")*"+str(kakeruyatu)+"-"+str(a_list[i-1])+"*"+str(c_list[i]))
# kakeruyatu_2=kakeruyatu+c_list[i]
"""ここまでを繰り返す"""
# print(str(d_list[i])+"="+str(a_list[i-2])+"*"+str(kakeruyatu)+"-"+str(a_list[i-1])+"*"+str(kakeruyatu_2))
# print(str(d_list[i])+"="+str(a_list[i-2])+"*"+str(kakeruyatu)+"-("+str(a_list[i-3])+"-"+str(b_list[i-3])+"*"+str(c_list[i-3])+")*"+str(kakeruyatu_2))
# kakeruyatu_3=b_list[i-3]*c_list[i-3]+kakeruyatu
# print(str(d_list[i])+"="+str(a_list[i-3])+"*(-"+str(kakeruyatu)+")+"+str(b_list[i-3])+"*"+str(kakeruyatu_3))

# while s!=-1:
#     print(d_list[s])
#     s-=1
kx=1
ky=0
# print(str(d_list[i])+"="+str(a_list[i])+"-("+str(a_list[i-1])+"-"+str(b_list[i-1])+"*"+str(c_list[i-1])+")*"+str(c_list[i]))
print(str(d_list[i])+"="+str(a_list[i])+"*"+str(kx)+"-"+str(b_list[i])+"*"+str(c_list[i]))
# kx= -c_list[i]
ky=c_list[i]
while i!=0:
    kx=c_list[i-1]*c_list[i]+kx
    print(" ="+str(a_list[i])+"*"+str(kx)+"-"+str(a_list[i-1])+"*"+str(ky))
    ky=c_list[i]*kx+ky
    i-=1
    # print(" ="+str(a_list[i-1])+"*"+str(kx)+"-"+str(a_list[i-1])+"*"+str(ky))
    

