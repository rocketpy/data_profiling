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

