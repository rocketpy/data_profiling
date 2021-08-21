# pip install pygal

import pygal
import seaborn as sns


# Loading Dataset
df = sns.load_dataset('tips')

# Simple Bar Chart
bar_chart = pygal.Bar()  
bar_chart.add('Tip', df['tip'])  
bar_chart.render_to_file('bar_chart.svg')


# Double Bar Chart
bar_chart.add('Tip', df['tip'][:10])
bar_chart.add('Total Bill', df['total'][:10])
bar_chart.render_to_file('bar_chart_2.svg')


# Line Chart
line_chart = pygal.Line()
line_chart.add('Total', df['total'][:15])
line_chart.render_to_file('line.svg')


# Double Line Chart
line_chart.add('Total', df['total_bill'][:15])
line_chart.add('Tip', df['tip'][:15])
line_chart.render_to_file('line_2.svg')
 
