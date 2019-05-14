import matplotlib.pyplot as plt

print("tizenharmadik feladat")
n1 = int(input("Adj meg egy egész számot!: "))
n2 = int(input("Adj meg egy egész számot!: "))
a = []
for i in range(n1):
    a.append([])
    a[i].append(1)
    for j in range(1, i):
        a[i].append(a[i - 1][j - 1] + a[i - 1][j])
    if (n1 != 0):
        a[i].append(1)
for i in range(n1):
    print("")
    for j in range(0, i + 1):
        print((a[i][j]), end=" ")

plt.plot(a[n2], "go")
plt.show()
