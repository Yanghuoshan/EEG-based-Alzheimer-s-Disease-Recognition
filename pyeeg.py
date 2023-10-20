from numpy.fft import fft
from numpy import zeros, floor, log10, log, mean, array, sqrt, vstack, cumsum, ones, log2, std
from numpy.linalg import svd, lstsq
import time


def bin_power(X, Band, Fs):
    """Compute power in each frequency bin specified by Band from FFT result of
    X. By default, X is a real signal.

    Note
    -----
    A real signal can be synthesized, thus not real.

    Parameters
    -----------

    Band
        list

        boundary frequencies (in Hz) of bins. They can be unequal bins, e.g.
        [0.5,4,7,12,30] which are delta, theta, alpha and beta respectively.
        You can also use range() function of Python to generate equal bins and
        pass the generated list to this function.

        Each element of Band is a physical frequency and shall not exceed the
        Nyquist frequency, i.e., half of sampling frequency.

     X
        list

        a 1-D real time series.

    Fs
        integer

        the sampling rate in physical frequency

    Returns
    -------

    Power
        list

        spectral power in each frequency bin.

    Power_ratio
        list

        spectral power in each frequency bin normalized by total power in ALL
        frequency bins.

    """
    C = fft(X)
    C = abs(C)
    Power = zeros(len(Band) - 1);
    for Freq_Index in range(0, len(Band) - 1):
        Freq = float(Band[Freq_Index])  ## Xin Liu
        Next_Freq = float(Band[Freq_Index + 1])
        Power[Freq_Index] = sum(C[int(floor(Freq / Fs * len(X))):int(floor(Next_Freq / Fs * len(X)))])
    Power_Ratio = Power / sum(Power)
    return Power, Power_Ratio