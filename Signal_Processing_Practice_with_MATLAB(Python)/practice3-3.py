'''
 practice3-3.py
 2023/Jul/04 S.OHSAWA

 MATLABによる信号処理実習 P25 実習3.2
 エイリアシング現象を見てみよう
'''

import numpy as np
import matplotlib.pyplot as plt

import lib.signal_process as sp


def main():
    # 元信号を作る
    time_end = 2.0
    dt = 10**-3 # 連続時間の刻み幅（サンプリング周波数1[kHz]）
    time_array = np.arange(0, time_end, dt)
    angular_freq=2*np.pi*8
    dc_offset=1.0
    analog_signal_array = sp.create_signal(time_array, angular_freq=angular_freq, dc_offset=dc_offset)

    # 標本化された信号を作る
    sampling_rate = 20
    sampling_period = 1/sampling_rate
    sampling_time_array = np.arange(0,  time_end, sampling_period)
    digital_signal_array = sp.create_signal(sampling_time_array, angular_freq=angular_freq, dc_offset=dc_offset)

    # ホールド信号を計算する
    hold_signal = []
    hold_time = int(sampling_period/dt) # １サンプル当たりの刻み幅（ホールドしている時間）
    Nn = int(time_end / sampling_rate)# 時間区間での信号地の個数（サンプル個数）
    for k in range(len(digital_signal_array)):
        # ホールド中は同じ値を１サンプル当たりの刻み幅個分代入する
        hold_signal = np.append(hold_signal, np.full(hold_time,digital_signal_array[k]))

    # ローパスフィルタで遮断する
    fft = sp.calc_fft(hold_signal, sampling_rate)
    plt.stem(fft['freq'], fft['amp'], markerfmt=".")
    plt.grid()
    plt.show()

    lpf_fft = sp.calc_lpf(fft['spect'],fft['freq'],sampling_rate,cutoff_freq=0.2)
    ifft_time = sampling_period / dt * sp.calc_ifft(lpf_fft['spect'])

    plt.plot(time_array, analog_signal_array)
    plt.plot(time_array, ifft_time, linestyle="dashed")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()