# Declaring a function
def fun():
    print("Inside function")


# Calling function
fun()


def myFun1(*argv):
    for arg in argv:
        print(arg)


def myFun2(**kwargs):
    for key, value in kwargs.items():
        print("% s == % s" % (key, value))


# Driver code
print("Result of * args: ")
myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("\nResult of **kwargs")
myFun2(first='Geeks', mid='for', last='Geeks')


# Python program to
# verify pass by reference

def myFun(x):
    print("Value received:", x, "id:", id(x))


# Driver's code
x = 12
print("Value passed:", x, "id:", id(x))
myFun(x)
