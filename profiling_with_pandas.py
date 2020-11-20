#  https://pandas-profiling.github.io/pandas-profiling/docs/

# Seaborn Datasets : ['anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots',
# 'exercise', 'flights', 'fmri', 'gammas', 'iris', 'mpg', 'planets', 'tips', 'titanic']

import pandas as pd
import seaborn as sns
import pandas_profiling


car_crashes = sns.load_dataset('car_crashes')
# car_crashes.head()

df = sns.load_dataset('car_crashes')

# some info about df
# df.describe()
# df.info()
