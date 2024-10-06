n = int(input())

heightlist = [eval(i) for i in input().split(" ")]

for x in range(n):
    right = heightlist[x:]
    