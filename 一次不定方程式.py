
print("一次不定方程式を解こう！！")
print("ax+by=c")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(str(a)+"x+"+str(b)+"y="+str(c))
# cを１にしたい。。。
if c != 1 :
    a=a/c
    b=b/c
    c=1
print(int(a),"x+",int(b),"y=",int(c))
# ユークリッドの互除法する
