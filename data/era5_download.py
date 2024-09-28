# python file to download ERA5 reanalysis data from cds.climate.copernicus.eu

import cdsapi

dataset = "reanalysis-era5-pressure-levels"
client = cdsapi.Client()
year_range = list(range(1959, 2000))
for year in range(1959, 2000):
    print(year)
    client.retrieve(dataset, 
        {
            "product_type": ["reanalysis"],
            "variable": [
                "geopotential",
                "specific_humidity",
                "temperature",
                "u_component_of_wind",
                "v_component_of_wind"
            ],
            "year": str(year),
            "month": [
                "06", "07", "08",
                "09", "10", "11"
            ],
            "day": [
                "01", "02", "03",
                "04", "05", "06",
                "07", "08", "09",
                "10", "11", "12",
                "13", "14", "15",
                "16", "17", "18",
                "19", "20", "21",
                "22", "23", "24",
                "25", "26", "27",
                "28", "29", "30",
                "31"
            ],
            "time": [
                "00:00", "03:00", "06:00",
                "09:00", "12:00", "15:00",
                "18:00", "21:00"
            ],
            "pressure_level": ["250", "550", "850"],
            "data_format": "grib",
            "download_format": "unarchived",
            "area": [65, -133, 1, 2]
        },
        'era5_'+str(year)+'.grib')