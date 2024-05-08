'''
 practice5-1.py
 2023/Jul/12 S.OHSAWA

 MATLABによる信号処理実習 P48 実習5.1
 白色雑音を生成する
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp


def main():
    length = 2**10
    time_array = np.arange(0, length)
    signal_array = np.random.rand(length)
    fft = sp.calc_fft(signal_array, length)

    fig = plt.figure(figsize = (6,8))
    fig.suptitle(f'DFT ,')
    ax1 = fig.add_subplot(211)
    ax1.plot(time_array, signal_array)
    ax1.set_xlabel("time")
    ax1.set_ylabel('amplitude')
    ax1.set_title(f'wave : length={length}')
    plt.grid()
    
    ax2 = fig.add_subplot(312, xlabel="xlabel", ylabel='ylabel')
    ax2.plot(fft['freq'][fft['freq']>=0], fft['power'][fft['freq']>=0])
    ax2.set_xlabel("frequency")
    ax2.set_ylabel('power:X^2/N^2[dB]')
    delta_f = fft['freq'][1]-fft['freq'][0]
    ax2.set_title(f'normalized power spectrum : Δf={round(delta_f, 2)}')
    plt.grid()

    plt.subplots_adjust(hspace=0.5)
    plt.show()



if __name__ == '__main__':
    main()