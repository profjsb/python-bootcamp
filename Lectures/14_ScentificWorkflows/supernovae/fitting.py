"""Functions for determining contents of universe"""

import numpy as np
from matplotlib import pyplot as plt

from astropy.cosmology import FlatLambdaCDM
from astropy import units as u
from scipy.optimize import fmin


def plot_sn_data(z, mb, mb_err, cosmo=None):
    """Plot supernova data, optionally with cosmology.

    Parameters
    ----------
    z : ndarray
    mb : ndarray
    mb_err : ndarray
    cosmo : Cosmology, optional

    Returns
    -------
    fig : Figure
    """

    plt.errorbar(z, mb, yerr=mb_err, ls='none', color='0.2', marker='o', ms=1.)
    if cosmo is not None:
        zarr = np.linspace(0.05, 1.2, 200)
        mb_predict = cosmo.distmod(zarr).value - 19.3
        plt.plot(zarr, mb_predict, c="r")
    plt.xlabel("redshift")
    plt.ylabel("mB")

    return plt.gcf()


def chisq(params, z, mb, mb_err):
    cosmo = FlatLambdaCDM(H0=params[0], Om0=params[1])
    mb_predicted = cosmo.distmod(z).value - 19.3
    return np.sum(((mb - mb_predicted) / mb_err)**2)


def fit_cosmology(z, mb, mb_err):
    """Fit cosmology to a set of data.

    Parameters
    ----------
    z : ndarray
        SN redshifts.
    mb : ndarray
        Apparent peak magnitudes.
    mb_err : ndarray
        Uncertainties on apparent peak magnitudes.

    Returns
    -------
    cosmo : Cosmology
        Fitted cosmology.
    """

    H0, Om0 = fmin(chisq, [70.,0.3], args=(z, mb, mb_err))
    return FlatLambdaCDM(H0=H0, Om0=Om0)
