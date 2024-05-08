'''
 practice1-4.py
 2023/Jun/5 S.OHSAWA

 MATLABによる信号処理実習 P7 実習1.4
 複素信号を種々の座標で示してみよう
'''

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def func_z(n, omega=0.05):
    return np.exp( omega * math.pi * n * 1j)


def main():

    n = np.arange(0, 80, 1)

    # (1) 実部のディジタル信号、虚部のディジタル信号
    z_n = np.vectorize(func_z)(n)
    plt.figure(1)
    plt.subplot(211)
    plt.stem(n, z_n.real)
    plt.grid()

    plt.subplot(212)
    plt.stem(n, z_n.imag)
    plt.grid()

    plt.show()

    # (2) 虚部の絶対値、二乗、逆正接
    plt.figure(1)
    plt.subplot(311)
    plt.stem(n, abs(z_n.imag))
    plt.grid()

    plt.subplot(312)
    plt.stem(n, z_n.imag**2)
    plt.grid()

    plt.subplot(313)
    plt.stem(n, np.arctan(z_n.imag/z_n.real))
    plt.grid()

    plt.show()

    # (3) 虚部の絶対値、二乗、逆正接
    plt.scatter(z_n.real, z_n.imag)
    plt.grid()

    plt.show()

    # (4) 虚部の絶対値、二乗、逆正接
    fig = plt.figure(figsize = (8, 8))

    # 3DAxesを追加
    ax = fig.add_subplot(111, projection='3d')

    # Axesのタイトルを設定
    ax.set_title("Helix", size = 20)

    # 軸ラベルを設定
    ax.set_xlabel("n", size = 14)
    ax.set_ylabel("real", size = 14)
    ax.set_zlabel("imaginary", size = 14)

    # 曲線を描画
    ax.scatter(n, z_n.real, z_n.imag)

    plt.show()


if __name__ == '__main__':
    main()