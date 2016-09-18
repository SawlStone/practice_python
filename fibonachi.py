def fibonachi():
    fib_prev = 0
    fib_cur = 1
    while fib_cur > 0:
        #fib_cur == str(fib_cur)
        if len(str(fib_cur)) == 1000:
            print (fib_cur)
            ak = str(fib_cur)
            print(len(ak))
            break
        fib_sum = fib_cur + fib_prev
        fib_prev = fib_cur
        fib_cur = fib_sum

def fibon():
    x = 0
    y = 1
    for i in range(100000):
        x, y = y, x + y
        if len(str(y)) == 1000:
            print(y)
            ak = str(y)
            print(len(ak))
            break

import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Time: %f" % (time.time()-t))
        return res

    return tmp()
timer(fibonachi)
print(40*"*")
timer(fibon)
