'''
 practice5-3.py
 2023/Jul/14 S.OHSAWA

 MATLABによる信号処理実習 P55 実習5.3
 位相スペクトルを表示してみよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp


def main():
    length = 2**9
    time_end = 1.0
    sampling_period = time_end/(length -1)
    sampling_rate = int(1/sampling_period)

    print(f'sampling period={sampling_period}, sampling rate={sampling_rate}')

    time = np.arange(0, time_end, sampling_period)
    initial_phase_list = [-7*np.pi/16, -3*np.pi/16, 5*np.pi/16]

    # 描画
    fig = plt.figure(figsize = (10,7))
    fig.suptitle(f'w')
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(223)
    ax3 = fig.add_subplot(222)
    ax4 = fig.add_subplot(224)
    for initial_phase in initial_phase_list:
        signal_array = sp.create_signal(time, angular_freq=2*np.pi*22, phase=initial_phase)
        fft = sp.calc_fft(sp.pass_window_func(signal_array, window_type='hanning'), sampling_rate)
    
        ax1.plot(time, signal_array)
        ax2.plot(fft['freq'][fft['freq']>=0], fft['amp'][fft['freq']>=0])
        ax3.plot(fft['freq'][fft['freq']>=0], fft['phase'][fft['freq']>=0])
        ax4.plot(fft['freq'][fft['freq']>=0], fft['phase'][fft['freq']>=0])
   
    ax1.set_xlabel("time")
    ax1.set_ylabel('amplitude')
    ax1.set_title(f'original signal')
    ax1.grid()
    
    ax2.set_xlabel("time")
    ax2.set_ylabel('amplitude')
    ax2.set_title('Signal multiplied by window function')
    ax2.grid()

    ax3.set_xlabel("frequency")
    ax3.set_ylabel('power:X^2/N^2')
    ax3.set_title(f'normalized power spectrum')
    ax3.grid()

    ax4.set_xlabel("frequency")
    ax4.set_ylabel('power:X^2/N^2[dB]')
    ax4.set_title(f'normalized power spectrum')
    ax4.grid()
    
    plt.subplots_adjust(hspace=0.35)
    plt.show()

if __name__ == '__main__':
    main()