import requests, json

import xarray as xr


# Sample url for dataset
# https://gcoos5.geos.tamu.edu/thredds/dodsC/ROFS_latest/txla2_frc_f_latest.nc.html

# base (server) -> gcoos5.geos.tamu.edu
# service -> /thredds/
# protocol -> dodsC (this is opendap for TDS)
# datasetid -> ROFS_latest/txla2_frc_f_latest.nc

# Can use xarr to remote open the dataset.

def getResponseCode(url):
    response = requests.get(url)
    return response.status_code

def main():

    testUrl = "https://gcoos5.geos.tamu.edu/thredds/dodsC/ROFS_latest/txla2_frc_f_latest.nc.dods"
    testurl2 = f"{testUrl}#fillmismatch"
    print(getResponseCode(testurl2))


    remote_data = xr.open_dataset(
        testurl2,
        decode_cf=False)
    
    print(remote_data)


if __name__ == '__main__':
    main()