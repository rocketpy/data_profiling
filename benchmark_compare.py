#  Offical:  https://github.com/MSeifert04/simple_benchmark

# The goal of this package is to provide a simple way to compare
# the performance of different approaches for different inputs and to visualize the result.

#  Dependencies:  NumPy, pandas, matplotlib

#  python -m pip install simple_benchmark

#  example
import numpy as np
from simple_benchmark import benchmark


funcs = [sum, np.sum]
arguments = {i: [1]*i for i in [1, 10, 100, 1000, 10000, 100000]}
argument_name = 'list size'
aliases = {sum: 'Python sum', np.sum: 'NumPy sum'}
b = benchmark(funcs, arguments, argument_name, function_aliases=aliases)
