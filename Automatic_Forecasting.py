#  Prophet is a procedure for forecasting time series data based on an additive model

# PyPi: https://pypi.org/project/prophet/
# Docs: https://facebook.github.io/prophet/docs/quick_start.html

# pip install prophet
# pip install pystan==2.19.1.1


# Example usage

from prophet import Prophet

m = Prophet()
# m.fit(df)  # df is a pandas.DataFrame with 'y' and 'ds' columns
future = m.make_future_dataframe(periods=365)
# m.predict(future)

