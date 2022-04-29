def announce(f): # takes the hello function as input
    def wrapper():
        print("About to run the function....") # message 1
        f()  # hello function wrapped inside announce function
        print("Done with the function.")  # message 2
    return wrapper()

@announce
def hello():
    print("Hello world")

hello()