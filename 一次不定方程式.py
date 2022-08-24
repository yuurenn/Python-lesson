
q=13
p=36
def xgcd(a,b):
    prevx, nextx = 1, 0
    prevy, nexty = 0, 1
    while b:
        quotient = a//b
        nextx, prevx = prevx - quotient * nextx, nextx
        nexty, prevy = prevy - quotient * nexty, nexty
        a, b = b, a % b
        # print(a,b)
    return prevx, prevy,a

print(str(q)+"x+"+str(p)+"y=1")
xg=(xgcd(q,p))
print("x="+str(xg[0]))
print("y="+str(xg[1]))