'''
 practice1-3_signal_arithmetic.py
 2023/Jun/5 S.OHSAWA

 MATLABによる信号処理実習 P5 実習1.3
 信号の乗算を行ってみよう
'''

import numpy as np
import math
import matplotlib.pyplot as plt

def func_x(time, sigma=0.5, mu = 0):
    return math.exp(- (time - mu)**2 / (2 * sigma**2) ) /(math.sqrt(2*math.pi))

def func_y(time, omega=20):
    return math.cos(omega * time)

def main():

    time = np.arange(-3, 3, 0.001)

    x_time = np.vectorize(func_x)(time)
    y_time = np.vectorize(func_y)(time)
    z_time = np.multiply(x_time ,y_time) # アダマール積を計算

    plt.figure(1)
    plt.subplot(311)
    plt.plot(time, x_time)
    plt.grid()

    plt.subplot(312)
    plt.plot(time, y_time)
    plt.grid()

    plt.subplot(313)
    plt.plot(time, z_time)
    plt.grid()

    plt.show()


if __name__ == '__main__':
    main()