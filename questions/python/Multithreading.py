"""
Demonstrate multithreading.
https://www.youtube.com/watch?v=PJ4t2U15ACo

@author a.k
"""

from threading import Thread
import time
from typing import List


def calc_square(nums: List[int]):
    for n in nums:
        time.sleep(0.5)
        print('square:', n * n)
    return


def calc_cube(nums: List[int]):
    for n in nums * 2:
        time.sleep(0.5)
        print('cube:', n * n * n)
    return


if __name__ == '__main__':
    nums = [2, 3, 8, 9]
    t1 = time.time()
    calc_square(nums)
    calc_cube(nums)
    print('total time taken:', round(time.time() - t1, 2))  # approx 4 seconds

    print('----------------------------------------------')
    t2 = time.time()
    T1 = Thread(target=calc_square, args=(nums,))  # set up threads
    T2 = Thread(target=calc_cube, args=(nums,))
    T1.start()  # start threads
    T2.start()
    T1.join()  # main thread will wait until T1 and T2 finish executing before executing the rest of the main program
    T2.join()  # .join() means main thread will wait until child thread finished executing
    print('total time taken:', round(time.time() - t2, 2))  # approx 2 seconds

    "NOTE: \
    T1.start()\
    T1.join()\
    T2.start()\
    T2.join()\
    -> this is the same as serial execution"
