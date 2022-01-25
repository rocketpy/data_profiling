#  JoyPy is a one-function Python package based on matplotlib + pandas with a single purpose: drawing joyplots (a.k.a. ridgeline plots).

# PyPi: https://pypi.org/project/joypy/0.2.6/
# Github: https://github.com/leotac/joypy

# pip install joypy==0.2.6


import joypy
import pandas as pd

iris = pd.read_csv("data/iris.csv")
fig, axes = joypy.joyplot(iris)

