'''
 practice6-2.py
 2023/Jul/19 S.OHSAWA

 MATLABによる信号処理実習 P55 実習5.4
 制限は周波数をモデリングにより推定しよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp
import scipy.signal as signal


def main():
    sampling_rate = 16000
    sampling_period = 1/sampling_rate
    sample_points = 80

    time = np.arange(0, 80*sampling_period, sampling_period)

    wave= np.cos(2*np.pi*1200*time)
    noize = 0.4*np.random.randn(sample_points)
    signal = wave + noize

    fft = sp.calc_fft(signal, sampling_rate)

    lpf = sp.calc_lpf(fft['spect'], fft['freq'], cutoff_freq=2000)
    ifft_time = sp.calc_ifft(lpf['spect'])

    fig = plt.figure(figsize = (6,8))
    fig.suptitle(f'Ddfdfd,')
    ax1 = fig.add_subplot(311)
    ax1.plot(time, signal)
    ax1.plot(time, wave)
    ax1.set_xlabel("time")
    ax1.set_ylabel('amplitude')
    ax1.set_title(f'imput signal')
    plt.grid()


    ax2 = fig.add_subplot(312)
    ax2.plot(fft['freq'][fft['freq']>0],fft['power'][fft['freq']>0])
    ax2.set_xlabel("time")
    ax2.set_ylabel('amplitude')
    ax2.set_title(f'imput signal')
    plt.grid()

    ax3 = fig.add_subplot(313)
    ax3.plot(time, ifft_time)
    ax3.set_xlabel("time")
    ax3.set_ylabel('amplitude')
    ax3.set_title(f'imput signal')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()