STORM INTENSITY FORECAST README.TXT
--------------------------------------
Author - Ishan Singh Bhullar
Date- 26 September 2024
Contact- ishanbhullar@gmail.com
--------------------------------------

Notebooks and Scripts
=====================
Please refer to storm_forecast_report.pdf for Process Flow.

Notebooks and Scripts are listed here based on order of use.

1. storm_tracks_dataset.ipynb 
	- Used to clean IBTrACS data downloaded from https://www.ncei.noaa.gov/products/international-best-track-archive
	- Refer to enviroment_one.txt for information on packages to install
	- Outputs storm_tracks_data.csv

2. era5_download.py 
	- Used to download ERA5 data from  https://cds.climate.copernicus.eu/#!/home (account creation required)
	- Located in data/folder
	- Best if run on terminal
	- Downloads .grib files for each year from 1959 to 1999
	- Refer to enviroment_two.txt for information on packages to install

3. grib_load_all.ipynb
	- Reads .grib files and capstone_track_data.csv
 	- Extracts information from the .grib files based on capstone_track_data.csv 
	- Outputs <year>_data.csv files for each year from 1959 to 1999
	- NOTE: RUNS ONLY ON GOOGLE COLABORATORY DUE TO MEMORY LEAKAGE ISSUE WITH ONE OF THE PACKAGES
	- Packages and prerequisites are listed in the notebook.

4. concat_csv.py
	- Concatenates all the <year>_csv.data into one .csv file
	- Outputs final_data.csv
	- Located in data/ folder (has to run there)
	- Best if run on terminal

5. eda.ipynb
	- Reads final_data.csv 
	- This is where I perform all Feature Engineering and EDA
	- Outputs model_data.csv
	- Refer to enviroment_one.txt for information on packages to install

6. ml_modeling.ipynb
	- Reads model_data.csv
	- Contains all modeling and model evaluation code
	- Refer to enviroment_three.txt for information on packages to install


data
=====================

Folder containing all the relevant .csv files and python scripts necessary to acquire and use them.

Saved Models
=====================

I have saved GridSearchCV best models to save future computation time and ensure reproducability. 

Saved models are:
- randomForest_gridSearch.pkl
- XGBoost_gridsearch.pkl
- XGBoost_reg_alpha_gridsearch.pkl
- svm_grid.pkl 

They are coded into the notebooks, so they should run by themselves as long as they are in the same directory as 
ml_modleing.ipynb notebook.