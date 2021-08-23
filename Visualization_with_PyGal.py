# A python svg graph plotting library and creating interactive charts ! 

# PyPi: https://pypi.org/project/pygal/
# Docs: http://www.pygal.org/en/stable/index.html

# Chart types: http://www.pygal.org/en/stable/documentation/types/index.html
# Maps: http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html

# pip install pygal
# pip install pygal_maps_world

import pygal
import seaborn as sns  # just for datasets
from pygal.style import Style


# Loading Dataset
df = sns.load_dataset('tips')

# Simple Bar Chart
bar_chart = pygal.Bar()  
bar_chart.add('Tip', df['tip'])  
bar_chart.title = "Bla bla"
bar_chart.render_to_file('bar_chart.svg')
# bar_chart.render_in_browser()


# Customizing the graph and using a Style
custom_style = Style(colors=('#E80080', '#404040', '#9BC850'))
bar_chart = pygal.Bar(style=custom_style)
bar_chart.title = "Some text"
bar_chart.add("A", [0.95])
bar_chart.add("B", [1.25])
bar_chart.add("C", [1])
bar_chart.render_in_browser()


# Double Bar Chart
bar_chart.add('Tip', df['tip'][:10])
bar_chart.add('Total Bill', df['total'][:10])
bar_chart.render_to_file('bar_chart_2.svg')


# Horizontal bar diagram
line_chart = pygal.HorizontalBar()
line_chart.title = 'Browser usage in February 2012 (in %)'
line_chart.add('IE', 19.5)
line_chart.add('Firefox', 36.6)
line_chart.add('Chrome', 36.3)
line_chart.add('Safari', 4.5)
line_chart.add('Opera', 2.3)
line_chart.render()


# Line Chart
line_chart = pygal.Line()
line_chart.add('Total', df['total'][:15])
line_chart.render_to_file('line.svg')


# Double Line Chart
line_chart.add('Total', df['total_bill'][:15])
line_chart.add('Tip', df['tip'][:15])
line_chart.render_to_file('line_2.svg')


# Box Plot
box_plot = pygal.Box()
box_plot.title = 'Tips'
box_plot.add('Tip', df['tip'])
box_plot.render_to_file('box1.svg')


#  Funnel Chart
funnel_chart = pygal.Funnel()
funnel_chart.title = 'Total'
funnel_chart.add('Total', df['total_bill'][:15])
funnel_chart.add('Tip', df['tip'][:15])
funnel_chart.render_to_file('funnel.svg')


# Working with maps
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Some countries'
worldmap_chart.add('F countries', ['fr', 'fi'])
worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                                   'mk', 'ml', 'mm', 'mn', 'mo',
                                   'mr', 'mt', 'mu', 'mv', 'mw',
                                   'mx', 'my', 'mz'])
worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
worldmap_chart.render()
 
#  specify a value for a country
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Minimum deaths by capital punishement (source: Amnesty International)'
worldmap_chart.add('In 2012', {
  'af': 14,
  'bd': 1,
  'by': 3,
  'cn': 1000,
  'gm': 9,
  'in': 1,
  'ir': 314,
  'iq': 129,
  'jp': 7,
  'kp': 6,
  'pk': 1,
  'ps': 6,
  'sa': 79,
  'so': 6,
  'sd': 5,
  'tw': 6,
  'ae': 1,
  'us': 43,
  'ye': 28
})
worldmap_chart.render()
  
