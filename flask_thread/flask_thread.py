import time
from threading import Thread
# calculate square of a function
def square(num):
    for n in num:
        time.sleep(1)
        print("square number is",n * n)



# calculate cube of a function
def cube(num):
    for p in num:
        time.sleep(1)
        print("cube of a function",p * p * p)

val = [2,5,7,8.6,3,5,89,1,2,45,76,2,11,3,5,88,9,0,12,32,44,54,66,76,55]

# current time
t = time.time()
print("current time",t)

# square(val)
# cube(val)
t1 = Thread(target=square,args=(val,))
t2 = Thread(target=cube,args=(val,))

t1.start()
t2.start()

t1.join()
t2.join()

print("time after execution",time.time()-t)
