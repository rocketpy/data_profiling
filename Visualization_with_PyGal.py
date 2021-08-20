# pip install pygal


import pygal
import seaborn as sns


# Loading Dataset
df = sns.load_dataset('tips')

# Simple Bar Chart
bar_chart = pygal.Bar()  
bar_chart.add('Tip', df['tip'])  
bar_chart.render_to_file('bar_chart.svg')

