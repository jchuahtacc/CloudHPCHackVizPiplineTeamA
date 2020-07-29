#! /usr/bin/env python3
#
# 2020-07-28 
# Colton Grainger 
# CC-0 Public Domain

"""
Simple Example
https://plotly.com/python/county-choropleth/#simple-example
"""

import plotly.figure_factory as ff

fips = ['06021', '06023', '06027',
        '06029', '06033', '06059',
        '06047', '06049', '06051',
        '06055', '06061']
values = range(len(fips))

fig = ff.create_choropleth(fips=fips, values=values)
fig.layout.template = None

fig.show()

# comment out below to NOT show figure in Dash application at
# http://127.0.0.1:8050

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
