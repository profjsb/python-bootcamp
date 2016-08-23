"""Utilities for downloading data."""

import numpy as np
from astropy.io import fits

def read_sn_data(fname):
    """Read SN data from the second extension of a FITS file.

    Parameters
    ----------
    fname : str
        File name.

    Returns
    -------
    sne : dict of ndarray
        Dictionary of arrays with keys 'z', 'mb', 'mb_err', 'c', 'x1'
    """

    hdulist = fits.open(fname)
    sne = np.asarray(hdulist[2].data)

    return {'z': sne["z"].astype(np.float64),
            'mb': sne["mb.S2"].astype(np.float64),
            'mb_err': sne["e_mb.S2"].astype(np.float64),
            'c': sne["c.S2"].astype(np.float64),
            'x1': sne["x1.S2"].astype(np.float64)}

