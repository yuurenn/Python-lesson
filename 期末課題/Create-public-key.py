#素数を二つ用意する
from math import gcd, lcm
from operator import mod

import time

# 公開鍵は長ければ安全だが長すぎると計算ができない：現在では2048ビットの解読はほぼ不可能
# 、安全性と処理負荷のバランスを考慮したうえで、鍵長を決めることが大切
# 2048bit鍵長は617桁、DESでは、64ビット（8バイト）の鍵を使っている　
p=283#7216
q=317#9745
n=p*q
#q-1,p-1の最小公倍数を求める
l=lcm(q-1,p-1)

if p>q:
    max=p
else :
    max=q
#暗号鍵がｐｑｌである
####max<e<lかつｌと互いに素である数をeとする
for num in range(max+1,l-1):
    #gcd(m,n)=1の際、m,nが互いに素なる
    if gcd(l,num)==1:
        e=num
        break

#もしｎとeしかわからないときどのようにｐとｑを求めるのかを作りたかった

#nとeが公開鍵として公開できる
print("n="+str(n)+"=p*q="+str(p)+"*"+str(q))
print("e="+str(e))

#平文DOGを数字にして十進数に変換するその後暗号化する

#送信者が公開鍵で暗号化：
a=2398**e
print("平文は2398だよ")
# print(a)
c=mod(a,n)
print("暗号化できました")
print(c)
#ここから復号化
#受信者に戻ってくる一次不定方程式ed+Ly=1を解く

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

xg=(xgcd(e,l))
d=xg[0]
d=mod(d,l)
m=c**d
print("平文に戻ったかな？？")
print(mod(m,n))

#nを求める
####################素数を出す###########################
primes_list = []          # このリストに素数を保存していく
upper_lim   = 1000       # テキトーな数を設定

for integer in range(2, upper_lim + 1, 1): # 2-10000の整数に対して、
    if len(primes_list) < 1 :              # primes_listが空だったら、
        primes_list.append(integer)        # primes_listにinteger(=2)を追加する
    else:                                  # その他の場合（本題）、
        is_divisible = False               # integerが割り切れない、つまり素数であることを仮定する
        for prime in primes_list:          # 今までに保存された全ての素数"prime"について、
            if integer % prime == 0:       # integerがprimeで割り切れるならば
                is_divisible = True        # 割り切れます（つまり素数じゃない）
                break                      # そしたらもうこのforはやる意味がないです。
        # integerが合成数ならどっかのprimeでis_divisible = Trueになる
        if not is_divisible:               # すべてのprimeについてこの判定をしたのち、それでもなおis_divisible = Falseならばもうそれは素数
            primes_list.append(integer)    # integerを素数として認め、primes_listに追加する
###########################################################
# print(primes_list)
primes_list2=primes_list
for i in primes_list :
    #半素数に近づける
    if n<=i*i:
        break
z=primes_list.index(i)
y=z
print(z)
print(primes_list)
##素数と素数をかけてｎと同じ数を出してｐとｑを求める
#iが求めたいリストのなかの場所なのでそこから一つずつ大きくして片方は小さくすることで時間が短縮できるのではないのではないのか
for i in range(primes_list[z-1]):
    for j in reversed(range(primes_list[y-1])):
        # print(i,j)
        if n==i*j:
            break

print(i,j)

