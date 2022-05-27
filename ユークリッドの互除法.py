#出力する関数作成したかった

a_list=[]
b_list=[]
c_list=[]
d_list=[]
print("ユークリッドの互除法をしたい二つの数字を入力")
a=int(input("a:"))
b=int(input("b:"))
j=a#一次不定方程式で利用
i=0
result = divmod(a, b)
# print(result[0], result[1])
c=int(result[0])
d=int(result[1])
#sequence=[a,b,c,d]
print(str(a)+"="+str(b)+"*"+str(c)+"+"+str(d))
a_list.append(str(a))
b_list.append(str(b))
c_list.append(str(c))
d_list.append(str(d))
# 繰り返す
while d != 0:
    a=b
    b=d 
    result=divmod(a, b)
    c=int(result[0])
    d=int(result[1])
    print(str(a)+"="+str(b)+"*"+str(c)+"+"+str(d))
    a_list.append(str(a))
    b_list.append(str(b))
    c_list.append(str(c))
    d_list.append(str(d))
    i=i+1
print(a_list)
print(b_list)
print(c_list)
print(d_list)
print(i)
print("最大公約数",b)
# 一次不定方程式
while i==0:
    print(str(d_list[i])+"="+str(a_list[i])+"-"+str(b_list[i])+"+"+str(c_list[i]))
    i=i-1
