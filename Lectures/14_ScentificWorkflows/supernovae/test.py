
from astropy.cosmology import FlatLambdaCDM
import numpy as np
from numpy.testing import assert_allclose

import fitting

def test_fit_cosmology():
    """Test fitting cosmology on simulated data."""

    # Generate some fake data.
    cosmo = FlatLambdaCDM(H0=70., Om0=0.25)
    z = np.random.rand(200)
    mb = -19.3 + cosmo.distmod(z).value
    mberr = 0.2 * np.ones_like(z)

    # fit to fake data
    fitted_cosmo = fitting.fit_cosmology(z, mb, mberr)

    # check that fitted H0 value is same as input
    assert_allclose(cosmo.H0.value, fitted_cosmo.H0.value, rtol=1e-4)
