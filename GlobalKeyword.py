x = "Hi"

def myFunc():
    global x
    x = "Hello"
    print(x)

print(x)
myFunc()
print(x)

