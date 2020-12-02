#!/usr/bin/env python
# coding=utf-8
import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print(next(it))
    except StopIteration:
        print('over iteration!')
        sys.exit()
