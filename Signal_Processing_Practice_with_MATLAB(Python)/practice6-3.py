'''
 practice6-3.py
 2023/Jul/25 S.OHSAWA

 MATLABによる信号処理実習 P55 実習5.4
 制限は周波数をモデリングにより推定しよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp
import scipy.signal as signal


def main():
    N = 80
    w_cr = 1/4
    md = N/4
    m = np.arange(0, N)

    h = w_cr * np.sinc(w_cr * (m-md))

    plt.plot(h)

    
    plt.xlabel("time")
    plt.ylabel('amplitude')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()