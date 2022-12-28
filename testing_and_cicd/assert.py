def square(x):
    return x**2

x= int(input("Enter a number: "))
# if the value is true the following statement is ignored.
# BUT if the value is false, it throws assertion error.s
assert(square(x)==25)