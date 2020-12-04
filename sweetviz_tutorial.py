#  A pandas-based library to visualize and compare datasets !

# PyPi: https://pypi.org/project/sweetviz/
# GIT: https://github.com/fbdesignpro/sweetviz

# pip install sweetviz


import sweetviz as sv


my_report = sv.analyze(my_dataframe)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"
