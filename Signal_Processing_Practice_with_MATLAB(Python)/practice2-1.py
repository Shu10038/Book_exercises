'''
 practice2-1.py
 fourier_transform_of_analog_signals
 2023/Jun/8 S.OHSAWA

 MATLABによる信号処理実習 P7 実習2.1
 複素信号を種々の座標で示してみよう
'''

import numpy as np
import matplotlib.pyplot as plt

def get_Fourier_coefficient(k):
    return -2 * np.sin(np.pi * k *2) / (np.pi * k)

def main():

    time = np.arange(-np.pi, np.pi, 0.001)

    x_time = np.where((time > np.pi/2)|(time < -np.pi/2), 1, 0)

    print(x_time)

    plt.plot(time, x_time)
    plt.show()

    k= np.arange(1, 11, 1)
    a = [1]
    # a_k = np.vectorize(get_Fourier_coefficient)(k)
    a_k = -2 * np.sin(np.pi * k /2) / (np.pi * k)
    a.extend(a_k)
    plt.stem(np.append(0, k), a)
    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()