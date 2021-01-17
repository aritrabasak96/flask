import time
import multiprocessing


def user_1(seat,lock):

    time.sleep(0.1)

    if seat.value > 0:


        lock.acquire()
        seat.value = seat.value - 1
        lock.release()
        print("user_1 congratulation")

    else:
        print("user_1 sorry the seat is not available")

def user_2(seat,lock):

    time.sleep(3)
    if seat.value > 0:
        lock.acquire()
        seat.value = seat.value - 1
        lock.release()


    else:
        print("user_2 sorry the seat is not available")



if __name__ == "__main__":

    seat = multiprocessing.Value('i',1)
    lock = multiprocessing.Lock()

    t1 = multiprocessing.Process(target=user_1,args=(seat,lock,))
    t2 = multiprocessing.Process(target=user_2,args=(seat,lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("end of program",seat.value)
