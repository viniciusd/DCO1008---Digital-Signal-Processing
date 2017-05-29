import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from scipy.interpolate import interp1d


def _load_signal(name):
    try:
        sig = loadmat(name)
    except FileNotFoundError:
        raise
    condition = name.split('_')[-1]
    sig['t'] = sig.pop('t_%s' % condition).flatten()
    sig['hr'] = sig.pop('hr_%s' % condition).flatten()
    # Removes DC component
    sig['hr'] -= np.mean(sig['hr'])
    return sig


def _signal_fix_sample_rate(sig, rate):
    new_sig = dict()

    interp, ts = interp1d(sig['t'], sig['hr']), 1/rate

    new_sig['t'] = np.arange(sig['t'][0], sig['t'][-1], ts)
    new_sig['hr'] = interp(new_sig['t'])
    return new_sig


def signal_autocorr_plot(name):
    sig = _load_signal(name)
    plt.figure()
    plt.acorr(sig['hr'], usevlines=False, maxlags=35)
    plt.xlabel('Lags')
    plt.ylabel('Autocorrelation')
    plt.savefig('q2_acorr_%s.png' % name)


def signal_psd_plot(name):
    rate = 100
    sig = _load_signal(name)
    sig = _signal_fix_sample_rate(sig, rate)
    plt.figure()
    plt.psd(sig['hr']**2, Fs=rate)
    plt.savefig('q2_psd_%s.png' % name)

if __name__ == '__main__':
    signal_autocorr_plot('Hr_pre')
    signal_autocorr_plot('Hr_med')
    signal_psd_plot('Hr_pre')
    signal_psd_plot('Hr_med')
