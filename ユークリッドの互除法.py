#出力する関数作成

print("ユークリッドの互除法をしたい二つの数字を入力")
a=int(input("a:"))
b=int(input("b:"))
i=0
result = divmod(a, b)
print(result[0], result[1])
c=int(result[0])
d=int(result[1])
#sequence=[a,b,c,d]
print(str(a)+"="+str(b)+"*"+str(c)+"+"+str(d))
while d != 0:
    a=b
    b=d 
    result=divmod(a, b)
    c=int(result[0])
    d=int(result[1])
    print(str(a)+"="+str(b)+"*"+str(c)+"+"+str(d))

print("最大公約数",b)