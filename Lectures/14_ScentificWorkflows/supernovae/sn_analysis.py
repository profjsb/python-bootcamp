from urllib.request import urlopen
import os

def download_file(url, dst):
    """Download a file from `url`, save to `dst`"""

    r = urlopen(url)
    with open(dst, "wb") as f:
        f.write(r.read())

# download some light curve data. See http://cdsarc.u-strasbg.fr/viz-bin/Cat?cat=J%2FA%2BA%2F523%2FA7
snls_data_url = "http://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/fits?J%2FA%2BA%2F523%2FA7"
dst = "sndata.fits"
if not os.path.exists(dst):
    download_file(snls_data_url, dst)
