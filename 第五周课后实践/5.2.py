import time


def run_time():
    T1 = time.perf_counter()
    time.sleep(0.01)
    T2 = time.perf_counter()
    print("挂起时间为:%s毫秒" % ((T2 - T1) * 1000))
    T3 = time.perf_counter()
    time.sleep(0.1)
    T4 = time.perf_counter()
    print("挂起时间为:%s毫秒" % ((T4 - T3) * 1000))
    T5 = time.perf_counter()
    time.sleep(1)
    T6 = time.perf_counter()
    print("挂起时间为:%s毫秒" % ((T6 - T5) * 1000))


run_time()
