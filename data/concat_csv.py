# Python script to read .csv files using pandas
# and return a concatenated .csv file.

import pandas as pd
from tqdm import tqdm

# instatiate empty dataframe
df_concat = pd.DataFrame()

# define year range of files to concat
start_year = 1959
end_year = 1999

# loop to read individual .csv files and concat them to the dataframe
for year in tqdm(range(start_year, end_year + 1)):
    # read file into pandas dataframe
    temp_df = pd.read_csv(str(year)+'_data.csv', index_col=0)

    # concat file
    df_concat = pd.concat([df_concat, temp_df], axis=0, ignore_index=True)

# write dataframe to .csv file
df_concat.to_csv('final_data.csv', header=True)
print('Done!')