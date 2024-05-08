'''
 signal_process.py
 2023/Jul/04 S.OHSAWA

 MATLABによる信号処理実習用
 信号処理部分についてよく使う関数をライブラリ化
'''

import numpy as np
from scipy.fftpack import fft, ifft, fftfreq


def calc_fft(signal, sampling_rate):
    # FFT 、返り値を変更しやすいように辞書形式にしておく
    spect =  fft(signal)
    amp = 2.0 * np.abs(spect) / len(signal) 
    phase = np.degrees(np.arctan2(spect.imag, spect.real)) 
    freq =  fftfreq(len(signal), d=1.0/ sampling_rate)
    #fft_freq =  np.linspace(0, sampling_rate, len(fft_spect))
    power = amp ** 2
    power_db = 10 * np.log10(power/np.max(power)) #正規化パワースペクトル（最大値が0）
    return {'spect' :spect,
            'amp' : amp, 
            'phase' :phase ,
            'freq' :freq,
            'power': power,
            'power_db':power_db}


def calc_lpf(spect, freq, cutoff_freq):
    # Low-pass filter
    lpf_spect = spect.copy()
    lpf_spect[(freq > cutoff_freq)|(freq< -cutoff_freq)] = 0+0j

    return {'spect' :lpf_spect,
            'amp' : np.abs(lpf_spect) / (len(lpf_spect) / 2)}


def calc_ifft(lpf_spect):
    return ifft(lpf_spect)

def pass_window_func(signal, window_type='rectwin'):
    if window_type=='rectwin':return signal
    elif window_type=='hamming':
        window = np.hamming(len(signal))
    elif window_type=='hanning':
        window = np.hanning(len(signal))
    elif window_type=='blackman':
        window = np.blackman(len(signal))        
    else:
        print("Error in window function name")
        exit()
    return signal * window


def create_signal(time_array, amp=1.0, angular_freq=1.0, phase=0.0, dc_offset=0.0):
    return amp*np.cos(angular_freq*time_array + phase) + dc_offset


