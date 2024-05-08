'''
 support.py
 2023/Jul/04 S.OHSAWA

 MATLABによる信号処理実習用
 よく使う関数をライブラリ化
'''

import os
 
def make_dire(dire_name):
 
    if not os.path.exists(dire_name):
        return os.makedirs(dire_name)