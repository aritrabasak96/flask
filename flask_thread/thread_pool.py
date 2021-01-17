import multiprocessing
import time


def fun(num):
    s = 0
    for i in range(num):
        s += num * num
    return s


def fun2():
    val = 1;
    for x in range(1,10000000000):

        val = val * x
    return val


if __name__ == "__main__":

    t = time.time()
    print("initial time",t)

    p = multiprocessing.Pool()
    result =  p.map(fun,range(1000000))

    p.close()
    p.join()

    # val =  fun2()
    print("end time",time.time()-t)
    # print(result)
