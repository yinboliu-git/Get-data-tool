#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/10/2021 11:49 PM
#@Author : Liu
#@File : 多线程.py
#@Software : PyCharm

import time
from multiprocessing.dummy import Pool

state_time = time.time()
def get_sum(a):
    time.sleep(2)
    return a[0]+a[1]


a_list = [(1,2),(2,2),(4,1),(2,4)]

pool_get = Pool(4)

b_list = pool_get.map_async(get_sum, a_list) #非阻塞式的多进程

pool.get.wait()
print('结束了...')

pool_get.close()
pool_get.join()
print(b_list)

print(b_list.get())
end_time = time.time()

print(end_time-state_time)

input(">>")
