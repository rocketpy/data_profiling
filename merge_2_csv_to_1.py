import pandas as pd


first = pd.DataFrame.from_csv("https://.csv")
second = pd.DataFrame.from_csv("https://.csv")

result = pd.merge(first, 
                  second, 
                  how='inner', 
                  left_on="second_id", 
                  right_on="id", 
                  sort=True,
                  suffixes=('_first', '_second'))
