'''
 practice3-2.py
 2023/Jun/28 S.OHSAWA

 MATLABによる信号処理実習 P25 実習3.2
 A-D変換
'''

import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

import lib.signal_process as sp




def main():
    time_end = 2.0
    dt = 10**-3 # 連続時間の刻み幅（サンプリング周波数1[Hz]）
    time_array = np.arange(0, time_end, dt)
    amp=9.5
    angular_freq=2.0*np.pi
    dc_offset=9.5
    analog_signal_array = sp.create_signal(time_array,amp=amp, angular_freq=angular_freq ,dc_offset=dc_offset) # 元信号

    # 標本化
    digital_sampling_period = 0.1 # デジタル信号のサンプリング間隔（サンプリング周波数10[Hz]）
    digital_sampling_period_array = np.arange(0, time_end, digital_sampling_period)
    digital_signal_array = sp.create_signal(digital_sampling_period_array,amp=amp, angular_freq=angular_freq ,dc_offset=dc_offset)

    # 量子化
    quantized_digital_signal_array = np.round(digital_signal_array)

    # 二進数化
    bin_signal_array = [bin(int(x)) for x in quantized_digital_signal_array]

    # 二進数化を10進数に戻す
    decimal_signal_array = [int(x,2) for x in bin_signal_array]

    # ホールド信号を計算する
    hold_processed_signal = []
    hold_processing_time = int(digital_sampling_period/dt)
    for k in range(len(decimal_signal_array)):
        hold_processed_signal = np.append(hold_processed_signal, np.full(hold_processing_time,decimal_signal_array[k]))

    # 量子化デジタル信号とホールド信号を描画する
    plt.plot(time_array, hold_processed_signal)
    plt.stem(digital_sampling_period_array, decimal_signal_array,"--")
    plt.grid()
    plt.show()

    # 周波数領域に変換して描画
    sampling_rate =  1/digital_sampling_period
    fft = sp.calc_fft(hold_processed_signal, sampling_rate)
    plt.stem(fft['freq'] ,fft['amp'])
    plt.grid()
    plt.show()

    # ローパスフィルタで遮断して周波数領域を描画する
    cutoff_freq = 0.05
    # cutoff_samp = int(np.round((len(decimal_signal_array)-1)*cutoff_freq/samplerate)) # 遮断周波数の周波数サンプル数
    # lpf = np.zeros(len(decimal_signal_array))
    # print(cutoff_samp)
    # lpf[0:cutoff_samp] = 1
    # print(len(lpf),len(freq))
    # cutoff_amp = amp* lpf
    lpf_fft = sp.calc_lpf(fft['spect'], fft['freq'], sampling_rate, cutoff_freq)


    plt.stem(fft['freq'], lpf_fft['amp'], markerfmt=".")
    plt.grid()
    plt.show()

    # cutoff_spectrum = spectrum* lpf
    ifft_time = sp.calc_ifft(lpf_fft['spect'])
    plt.plot(time_array, analog_signal_array)
    plt.plot(time_array, ifft_time)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()