def divide(x,y):
    print(x,y)
def outer_fun(func):
    def inner(x,y):
        if x<y:
            x,y=x,y
        return func(x,y)
    return inner

@outer_fun#decorator used to add method in a function
def divide(x,y):
    print(x/y)
divide(24,2)
