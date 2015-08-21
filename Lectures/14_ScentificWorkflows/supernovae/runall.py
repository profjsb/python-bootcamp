#!/usr/bin/env python
"""Script to run entire SN analysis."""

import os

import data_utils
import fitting

DATA_URL = ("http://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/"
            "fits?J%2FA%2BA%2F523%2FA7")

data_fname = os.path.join("..", "data", "sndata.fits")
plot_fname = os.path.join("..", "plots", "cosmofit.png")
results_fname = os.path.join("..", "results", "results.txt")

# download the data if we haven't already done so.
if not os.path.exists(data_fname):
    print("downloading data...")
    data_utils.download_file(DATA_URL, data_fname)

sne = data_utils.read_sn_data(data_fname)

# Correct mb with known correction factors.
sne["mb_corr"] = sne["mb"] - 2.3 * sne["c"] + 0.128 * sne["x1"]

print("Fitting cosmology to data...")
cosmo = fitting.fit_cosmology(sne["z"], sne["mb_corr"], sne["mb_err"])

print("Plotting results to", plot_fname)
fig = fitting.plot_sn_data(sne["z"], sne["mb_corr"], sne["mb_err"],
                           cosmo=cosmo)
fig.savefig(plot_fname)

print("Writing results file to", results_fname)
with open(results_fname, "w") as f:
    f.write("H0,Om0\n{},{}\n".format(cosmo.H0.value, cosmo.Om0))

