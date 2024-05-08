'''
 practice2-2.py
 2023/Jun/5 S.OHSAWA

 MATLABによる信号処理実習 P7 実習1.4
 周波数スペクトルを表示しよう
'''

import numpy as np
import math
import matplotlib.pyplot as plt


def calc_amplitude_spectrum(w, w0):
    return np.sqrt(1+np.multiply(w,w))/np.sqrt((1-w0**2+np.multiply(w,w))**2+4*np.multiply(w,w))

def calc_phase_spectrum(w, w0):
    return np.arctan(-np.multiply(w,(np.multiply(w,w)-w0**2+1))/(1+w0**2+np.multiply(w,w)))

def func_x(f0, t):
    return np.exp(-t)*np.cos(2*np.pi*f0*t)


def show_frequency_spectrum(f0, time ,dt):

    x_a = [func_x(f0, t) if t>=0 else 0 for t in time] # np.vectorize(calc_x_a)(f0, time)
    w0 = 2*np.pi*f0
    # 振幅
    plt.title(f'analog signal:f0={f0}')
    plt.plot(time, x_a)
    plt.grid()
    plt.show()
    
    # (2) 虚部の絶対値、二乗、逆正接
    fs = 1/dt
   
    w = np.linspace(-fs/2, fs/2, len(x_a))
    amp_spect_array = calc_amplitude_spectrum(w, w0)
    plt.figure(1)
    plt.subplot(311)
    plt.plot(w, amp_spect_array)
    plt.grid()

    phase_spect_array = calc_phase_spectrum(w, w0)
    plt.subplot(312)
    plt.plot(w, phase_spect_array)
    plt.grid()

    plt.subplot(313)
    plt.plot(w, np.multiply(amp_spect_array,amp_spect_array))
    plt.grid()

    plt.show()

def main():

    te = 10
    dt = 0.01
    time = np.arange(-te, te, dt)

    f0 = 0
    show_frequency_spectrum(f0, time, dt)

    f0 = 5
    show_frequency_spectrum(f0, time, dt)


if __name__ == '__main__':
    main()