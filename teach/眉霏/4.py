a = input().split()
b= str(a[0])
ans = []
shift = int(a[1])
for i in b :
     c = None
     if i.islower():
          c = "a"
     else:
          c="A"
     ans.append(chr((ord(i)-ord(c)+shift)%26+ord(c)))
print(ans)
