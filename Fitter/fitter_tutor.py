# Fitter - A tool to fit data to many distributions and best one(s)

# PyPi: https://pypi.org/project/fitter/
# Github: https://github.com/cokelaer/fitter
# Docs: https://fitter.readthedocs.io/en/latest/

# Installation: pip install fitter

# Compatible with Python 3.6, 3.7, and 3.8, 3.9

# A standalone application (very simple) is also provided and works with input CSV files,
# It creates a file called fitter.png and a log fitter.log
# fitter fitdist data.csv --column-number 1 --distributions gamma,normal

# Example
from scipy import stats
from fitter import Fitter

# creating a data
data = stats.gamma.rvs(2, loc=1.5, scale=2, size=10000)

f = Fitter(data)
f.fit()
# may take some time since by default, all distributions are tried
# but you call manually provide a smaller set of distributions
f.summary()

