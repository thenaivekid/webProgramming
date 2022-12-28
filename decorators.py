#decorators controls the function
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper


# @announce   #using decorator for the function
# def hello():
#     print("Hello, world!")

# hello()
# hello()
# hello()