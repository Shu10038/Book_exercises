'''
 practice3-1.py
 2023/Jun/13 S.OHSAWA

 MATLABによる信号処理実習 P23 実習3.1
 A-D変換
'''

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_signal_array(time_array, gain=9.5):
    return gain*np.cos(2*np.pi*time_array)+gain


def main():
    time_end = 2.0
    dt = 10**-3 # 連続時間の刻み幅（サンプリング周波数1[Hz]）
    time_array = np.arange(0, time_end, dt)
    analog_signal_array = create_signal_array(time_array) # 元信号

    # 標本化
    digital_sampling_period = 0.1 # デジタル信号のサンプリング間隔（サンプリング周波数fa=10[Hz]）
    digital_sampling_period_array = np.arange(0, time_end, digital_sampling_period)
    digital_signal_array = create_signal_array(digital_sampling_period_array)

    # 量子化
    quantized_digital_signal_array = np.round(digital_signal_array)

    # (1) アナログ信号とサンプル信号
    plt.figure(1)
    plt.subplot(311)
    plt.plot(time_array, analog_signal_array)
    plt.grid()

    plt.subplot(312)
    plt.stem(digital_sampling_period_array, digital_signal_array)
    plt.grid()

    plt.subplot(313)
    plt.stem(digital_sampling_period_array, quantized_digital_signal_array)
    plt.grid()

    plt.show()

    # (1) アナログ信号とサンプル信号
    plt.figure(1)
    plt.scatter(digital_sampling_period_array, digital_signal_array, marker="o",color="r", alpha=0.7)
    plt.scatter(digital_sampling_period_array, quantized_digital_signal_array, marker="o",color="b", alpha=0.7)
    plt.grid()

    plt.show()

    # 符号化


if __name__ == '__main__':
    main()