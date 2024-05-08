'''
 practice4-2.py
 2023/Jul/06 S.OHSAWA

 MATLABによる信号処理実習 P25 実習3.2
 エイリアシング現象を見てみよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp


def calc_dft(sampling_interval, start_time, length):
    time_array = np.arange(start_time, start_time + length, sampling_interval)
    angular_freq = 2*np.pi
    sampling_rate = 1/sampling_interval
    
    # 信号を作る
    signal_array = sp.create_signal(time_array, angular_freq=angular_freq)
    
    fft = sp.calc_fft(signal_array, sampling_rate)

    fig = plt.figure(figsize = (6,8))
    fig.suptitle(f'DFT : start_time={start_time}, sampling_interval={sampling_interval},')
    ax1 = fig.add_subplot(311)
    ax1.plot(time_array, signal_array)
    ax1.set_xlabel("time")
    ax1.set_ylabel('amplitude')
    ax1.set_title(f'wave : length={length}')
    plt.grid()
    
    ax2 = fig.add_subplot(312, xlabel="xlabel", ylabel='ylabel')
    ax2.plot(fft['freq'][fft['freq']>=0], fft['power_db'][fft['freq']>=0])
    ax2.set_xlabel("frequency")
    ax2.set_ylabel('power:X^2/N^2[dB]')
    delta_f = fft['freq'][1]-fft['freq'][0]
    ax2.set_title(f'normalized power spectrum : Δf={round(delta_f, 2)}')
    plt.grid()

    ax3 = fig.add_subplot(313, xlabel="xlabel", ylabel='ylabel')
    ax3.plot(fft['freq'][0:30], fft['power'][0:30])
    ax3.set_xlabel("frequency")
    ax3.set_ylabel('amp:X^2/N^2')
    ax3.set_title('spectrum')
    plt.grid()

    plt.subplots_adjust(hspace=0.5)
    plt.show()

def main():
    sampling_interval = [0.005, 0.005, 0.001, 0.006]
    start_time = [0.0, 0.02, 0.0 ,0.0]
    length = [3.0, 2.4, 2.0,7.0]
    for si, st, l in zip(sampling_interval, start_time, length):
        calc_dft(si, st, l)

if __name__ == '__main__':
    main()