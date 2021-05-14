import pandas as pd
from pandas_profiling import ProfileReport

report = pandas_profiling.ProfileReport(df,
                                        check_recoded=False,
                                        check_correlation_pearson=False,
                                        check_correlation_cramers=False,
                                        missing_diagrams={'bar': False,
                                                          'matrix': False,
                                                          'heatmap': False,
                                                          'dendrogram': False
                                                           }
                                        )

"""
Advanced usage

A set of options is available in order to adapt the report generated.

title (str): Title for the report ('Pandas Profiling Report' by default).
pool_size (int): Number of workers in thread pool. When set to zero, it is set to the number of CPUs available (0 by default).
progress_bar (bool): If True, pandas-profiling will display a progress bar.
infer_dtypes (bool): When True (default) the dtype of variables are inferred using visions using the
typeset logic (for instance a column that has integers stored as string will be analyzed as if being numeric).
"""
# Example

profile = df.profile_report(title="Pandas Profiling Report", plot={"histogram": {"bins": 8}})
profile.to_file("output.html")

