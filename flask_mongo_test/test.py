def outer(f):
    def inner(x,y):
        data = f(x,y)
        print(data)
        return 'hello'
    return inner

@outer  # outer(m1)
def m1(a,b):
    return 'm1'

m1()
