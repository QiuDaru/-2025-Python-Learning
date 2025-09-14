n = int(input())
date= {}
for i in range(n):
    s,g = input().split()
    date[s] = g
print(max(date,key=date.get)) 
x = ("c a b").split("a")