print("一次不定方程式 ax + by = 1 を解くプログラム")

# 途中経過を入れる配列
a = [] # 割られる数
b = [] # 割る数
q = [] # 商
r = [] # 余り
kx = [] # xの係数
ky = [] # yの係数

i = 0 # リストの先頭に位置する
j = 0 # リストの先頭に位置する

a.append(int(input("a=")))
b.append(int(input("b=")))

print("ユークリッドの互除法")
q.append(a[i] // b[i]) # 商をリストの先頭に追加
r.append(a[i] % b[i])  # 余りをリストの先頭に追加
print("(",i,")", a[i], "=", b[i], "*", q[i], "+", r[i])

# 余りが0になるまで割る
while r[i] != 0:
  a.append(b[i]) # 割られる数を割る数にする
  b.append(r[i]) # 割る数をあまりにする
  i += 1         # リストの位置を一つ更新
  q.append(a[i] // b[i])
  r.append(a[i] % b[i])
  print("(",i,")", a[i], "=", b[i], "*", q[i], "+", r[i])

print()
print("最大公約数は", b[i])

print()
print("一次不定方程式を解く")

i -= 1
kx.append(1)
ky.append(-q[i])
print("(",i,")", "1 =",  "(",kx[j],")",  "*", a[i], "+", "(",ky[j],")", "*", b[i])

# 0行目まで繰り返す
while i != 0:
  i -= 1 # 一行下へ
  kx.append(ky[j])
  ky.append(kx[j] + (q[i])*(-ky[j]))
  j += 1 # リストの位置を一つ更新
  print("(",i,")", "  =",  "(",kx[j],")",  "*", a[i], "+", "(",ky[j],")", "*", b[i])

# 結果を出力
print(a[i], "x", b[i], "y = 1 の解は")
print("特殊解 x0 =", kx[j], " y0 =", ky[j])
print("x = ", kx[j], "+", b[i], " *t")
print("x = ", ky[j], "-", a[i], " *t")