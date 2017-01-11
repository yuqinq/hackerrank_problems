import sys


n = int(input().strip())
bin_n = str(bin(n))
n_1 = bin_n.strip("0b").split("0")
print(max(len(n_1[i]) for i in range(len(n_1))))
