
a=3
b=2
c=4
d=7
n=36
print([[a,b],[c,d]])
rinmat=[[d,-b],[-c,a]]
print(rinmat)
fa=a*d-c*b
print(str(fa)+"x="+str(n)+"y+1")

def inv(a, b):
    if a == 1:
        return 1
    else:
        return b + (-b * inv(b % a, a) + 1) // a
x=inv(fa,n)
y=(fa*x-1)/n
print(x,y)
q=0
l = list(range(0))
for listn in rinmat:
    for element in listn:
        element=element*x
        print(element)
        q=q+1
        l.append(element)

l2=list(range(0))
for list in l:
    list=list%n
    l2.append(list)

print(l2)