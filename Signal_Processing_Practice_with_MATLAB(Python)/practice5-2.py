'''
 practice5-2.py
 2023/Jul/13 S.OHSAWA

 MATLABによる信号処理実習 P54 実習5.2
 相互相関関数を用いてパワースペクトルを表示する、窓関数の挙動を確認する
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp


def WienerKhinchin_theorem(signal):
    corr = np.correlate(signal, signal, "same")
    return sp.calc_fft(corr, 2^7)

def draw(time_array, signal_array, window_type):
    # 窓関数をかけてウィーナー＝ヒンチンの定理に基づいて計算する
    win_signal_array = sp.pass_window_func(signal_array, window_type=window_type)
    fft = WienerKhinchin_theorem(win_signal_array)
    
    # 描画
    fig = plt.figure(figsize = (10,7))
    fig.suptitle(f'window type={window_type}')
    ax1 = fig.add_subplot(221)
    ax1.plot(time_array, signal_array)
    ax1.set_xlabel("time")
    ax1.set_ylabel('amplitude')
    ax1.set_title(f'original signal')
    plt.grid()
    
    ax2 = fig.add_subplot(223)
    ax2.plot(time_array, win_signal_array)
    ax2.set_xlabel("time")
    ax2.set_ylabel('amplitude')
    ax2.set_title('Signal multiplied by window function')
    plt.grid()

    ax3 = fig.add_subplot(222)
    ax3.plot(fft['freq'][fft['freq']>=0], fft['power'][fft['freq']>=0])
    ax3.set_xlabel("frequency")
    ax3.set_ylabel('power:X^2/N^2')
    ax3.set_title(f'normalized power spectrum')
    plt.grid()

    ax4 = fig.add_subplot(224)
    ax4.plot(fft['freq'][fft['freq']>=0], fft['power_db'][fft['freq']>=0])
    ax4.set_xlabel("frequency")
    ax4.set_ylabel('power:X^2/N^2[dB]')
    ax4.set_title(f'normalized power spectrum')
    plt.grid()
    
    plt.subplots_adjust(hspace=0.35)
    plt.show()

def main():
    length = 2**7
    time_array = np.arange(0, length)

    F1 = 2.4/8.0 # 正規化周波数値：0.3
    F2 = 2.24/8.0 # 正規化周波数値：0.28
    signal_array = np.cos(2*np.pi*F1*time_array)+np.sin(2*np.pi*F2*time_array) + np.random.normal(0, 0.5, (len(time_array)))

    window_type_list = ['rectwin', 'hanning', 'hamming', 'blackman']
    for wt in window_type_list:
        draw(time_array, signal_array, wt)


if __name__ == '__main__':
    main()