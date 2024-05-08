'''
 practice6-1.py
 2023/Jul/19 S.OHSAWA

 MATLABによる信号処理実習 P55 実習6.1
 畳み込み演算を行ってみよう
'''

import numpy as np
import matplotlib.pyplot as plt

def convolution(time):
    tu = 5
    if 0 <=time and time <= tu:
        return 1- np.exp(-time)
    elif time > tu:
        return np.exp(-time)* (np.exp(tu) - 1 )
    else:
        return 0

def main():
    time_end = 40.0
    dt = 0.01
    time_array = np.arange(-time_end/2, time_end/2, dt)

    numb_data = np.arange(-len(time_array)/2 ,len(time_array)/2)
    tu = 5.0

    imput_signal = [1 if t >= 0 and t <= tu else 0 for t in time_array]
    impulse_response = [np.exp(-t) if t >= 0 else 0 for t in time_array]
    output_signal = [convolution(t) for t in time_array]

    fig = plt.figure(figsize = (6,8))
    fig.suptitle(f'convolution')
    ax1 = fig.add_subplot(311)
    ax1.plot(time_array, imput_signal)
    ax1.set_xlabel("time")
    ax1.set_ylabel('amplitude')
    ax1.set_title(f'imput signal')
    plt.grid()

    ax2 = fig.add_subplot(312)
    ax2.plot(time_array,impulse_response)
    ax2.set_xlabel("time")
    ax2.set_ylabel('amplitude')
    ax2.set_title(f'imput signal')
    plt.grid()

    ax3 = fig.add_subplot(313)
    ax3.plot(time_array,output_signal)
    ax3.set_xlabel("time")
    ax3.set_ylabel('amplitude')
    ax3.set_title(f'imput signal')

    plt.subplots_adjust(hspace=0.5)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()