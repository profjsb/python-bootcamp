#!/usr/bin/env python

import os
from urllib.request import urlopen


def download_file(url, dst):
    """Download a file from url, save to dst"""
    r = urlopen(url)
    with open(dst, "wb") as f:
        f.write(r.read())


data_url = ("http://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/"
            "fits?J%2FA%2BA%2F523%2FA7")
os.makedirs("data", exist_ok=True)
download_file(data_url, os.path.join("data", "sndata.fits"))
