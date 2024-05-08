'''
 practice8-1.py
 2023/Jul/25 S.OHSAWA

 MATLABによる信号処理実習 P55 実習5.4
 制限は周波数をモデリングにより推定しよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp
import scipy.signal as signal


def main():
    sampling_rate = 8000
    sampling_period = 1/sampling_rate
    sample_points = 80

    time = np.arange(0, 0.1, sampling_period)
    samples = np.arange(0, len(time))

    signal = np.cos(2*np.pi*800*time) + np.cos(2*np.pi*3100*time)

    # fft = sp.calc_fft(signal, sampling_rate)

    # lpf = sp.calc_lpf(fft['spect'], fft['freq'], cutoff_freq=2000)
    # ifft_time = sp.calc_ifft(lpf['spect'])

    fig = plt.figure(figsize = (6,8))
    fig.suptitle(f'Ddfdfd,')
    ax1 = fig.add_subplot(111)
    ax1.plot(time[time<=0.02], signal[time<=0.02])

    ax1.set_xlabel("time")
    ax1.set_ylabel('amplitude')
    ax1.set_title(f'imput signal')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()