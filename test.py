# -*- coding: utf-8 -*-
"""
Created on 2018/5/22 

@author: susmote
"""

with open('right_code.txt' ,'r+') as f:
    f_list = f.readlines()
    f_list_len = len(f_list)
    f_list[f_list_len - 1] = 'asdf\n'
    with open('right_code.txt', 'w+') as f_w:
        for i in range(f_list_len):
            f_w.writelines(f_list[i])
        f.close()