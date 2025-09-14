def f(i):

 if i > 0:
     if (i // 2) % 2 == 0:
        print(1)
        return f(i - 2) * i
     print(2)
     return f(i - 2) * (-i)
 else:
    print(3)
    return 1
print(f(10))