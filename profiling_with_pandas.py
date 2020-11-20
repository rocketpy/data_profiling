#  https://pandas-profiling.github.io/pandas-profiling/docs/

# Seaborn Datasets : ['anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots',
# 'exercise', 'flights', 'fmri', 'gammas', 'iris', 'mpg', 'planets', 'tips', 'titanic']

# pip install pandas-profiling

import pandas as pd
import seaborn as sns
import pandas_profiling


car_crashes = sns.load_dataset('car_crashes')
# car_crashes.head()

df = sns.load_dataset('car_crashes')

# some info about df
# df.describe()
# df.info()

profile = pandas_profiling.ProfileReport(df)
profile.to_file("Car_crashes.html")  # outputfile="Car_crashes.html"
#  or
df = pd.read_csv('file_name.csv')
profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="file_name.html")
