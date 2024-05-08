'''
 practice4-1.py
 2023/Jul/06 S.OHSAWA

 MATLABによる信号処理実習 P25 実習3.2
 エイリアシング現象を見てみよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp


def main():
    # 元信号を作る
    time_end = 2.0
    dt = 0.2
    sampling_rate = 1/dt
    time_array = np.arange(0, time_end, dt)
    angular_freq=2*np.pi
    signal_array = sp.create_signal(time_array, angular_freq=angular_freq)

    fft = sp.calc_fft(signal_array, sampling_rate)
    plt.stem(fft['freq'], fft['amp'], markerfmt=".")
    plt.grid()
    plt.show()

    pow_spect = np.multiply(fft['spect'],np.conj(fft['spect']))
    
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax1.stem(signal_array)
    ax2 = fig.add_subplot(2,1,2)
    ax2.stem(pow_spect)
    plt.show()

   

if __name__ == '__main__':
    main()