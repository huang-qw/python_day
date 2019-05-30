def foo4():
    global b
    b = 200  #全局变量
    print(b)

foo4()
print(b)