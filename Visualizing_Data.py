import pandas as pd
import numpy as np
import requests


# get a data
df_stream_0 = pd.read_json('data_1.json')
df_stream_1 = pd.read_json('data_2.json')

# merge dataframes
df_stream = pd.concat([df_stream_0, df_stream_1])

# create a unique ID
df_stream['UniqueID'] = df_stream['Name'] + ":" + df_stream['Surname']
# df_stream.head()

# json file into a pandas dataframe
df_library = pd.read_json('Library_1.json')

# add Unique ID columт
df_library['UniqueID'] = df_library['artist'] + ":" + df_library['track']

# add column
new = df_library["uri"].str.split(":", expand = True)
df_library['track_uri'] = new[2]

# df_library.head()


# create final dict
df_tableau = df_stream.copy()

# not used in this project but could be helpful for cool visualizations
# df_tableau['In Library'] = np.where(df_tableau['UniqueID'].isin(df_library['UniqueID'].tolist()),1,0)

# left join with df_library on UniqueID
df_tableau = pd.merge(df_tableau, df_library[['album','UniqueID','track_uri']],how='left',on=['UniqueID'])


