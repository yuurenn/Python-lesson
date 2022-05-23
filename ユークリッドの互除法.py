#出力する関数作成

print("ユークリッドの互除法をしたい二つの数字を入力")
a=int(input("a:"))
b=int(input("b:"))
i=0
result = divmod(a, b)
print(result[0], result[1])
print(str(a)+"="+str(b)+"*"+str(result[0])+"+"+str(result[1]))
Result = divmod(b,result[1])
print(Result[0], Result[1])
print(str(b)+"="+str(result[1])+"*"+str(Result[0])+"+"+str(Result[1]))
rEsult = divmod(result[1],Result[1])
print(rEsult[0], rEsult[1])
print(str(result[1])+"="+str(Result[1])+"*"+str(rEsult[0])+"+"+str(rEsult[1]))