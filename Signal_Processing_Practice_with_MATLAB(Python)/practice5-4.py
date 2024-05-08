'''
 practice5-4.py
 2023/Jul/18 S.OHSAWA

 MATLABによる信号処理実習 P55 実習5.4
 制限は周波数をモデリングにより推定しよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp
import scipy.signal as signal

def main():
    length = 2**12
    sampl = np.arange(0,length)
    ang_freq = 2 * np.pi / sampl

    noize = 0.3*np.random.rand(length)
    noise_free_signal = 0.8*np.sin(2*np.pi*0.1*sampl) + noize
    signal_array = noise_free_signal + noize

    pgram = signal.lombscargle(sampl, signal_array, ang_freq)

    plt.subplots_adjust(hspace=0.35)
    plt.plot(sampl, pgram)
    plt.show()

if __name__ == '__main__':
    main()