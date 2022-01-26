#  JoyPy is a one-function Python package based on matplotlib + pandas with a single purpose: drawing joyplots (a.k.a. ridgeline plots).

# PyPi: https://pypi.org/project/joypy/0.2.6/
# Github: https://github.com/leotac/joypy

# pip install joypy==0.2.6
# pip install joypy

# To install from github, run:
"""
git clone git@github.com:leotac/joypy.git
cd joypy
pip install .
"""

# IMPORTANT
"""
Dependencies:
    Python 3.5+
    Compatibility with python 2.7 has been dropped with release 0.2.0.
    numpy
    scipy >= 0.11
    matplotlib
    pandas >= 0.20 Warning: compatibility with pandas >= 0.25 requires joypy >= 0.2.1
"""

import joypy
import pandas as pd

iris = pd.read_csv("data/iris.csv")
fig, axes = joypy.joyplot(iris)

