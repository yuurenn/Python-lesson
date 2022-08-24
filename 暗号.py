x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!"

y = str(input("文字を入力してください．"))
n = int(input("文字数を入力してください．"))

a = []

for j in range(n):
    for i in range(27):
        if x[i] == y[j]:
            a.append(i)

p = int(input("前ずらし = 1, 後ずらし = 2"))

if p == 1:
    for k in range(26):
        print(k+1,"文字ずらし = ")
        for l in range(n):
            print(x[(a[l]-k-1)%27])
else:
    for k in range(26):
        print(k+1,"文字ずらし = ")
        for l in range(n):
            print(x[(a[l]+k+1)%27])

