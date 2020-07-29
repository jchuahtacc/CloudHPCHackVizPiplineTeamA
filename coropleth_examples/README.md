---
title: USA County Choropleth Maps
date: 2020-07-28
source: "https://plotly.com/python/county-choropleth"
copyright: 2020 Plotly.
---

## Learn you the command line for great good

These coropleth map examples exhibit a legacy "figure factory" method for creating map-like figures using self-filled scatter traces. 

The (depreciated) documentation for the function `plotly.figure_factory.create_choropleth` is here: 

<https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_choropleth.html>

**Beachtung!** This is no longer the recommended way to make county-level choropleth maps, instead we recommend using a GeoJSON-based approach to making outline choropleth maps or the alternative Mapbox tile-based choropleth maps.

## Required Packages

`geopandas`, `pyshp` and `shapely` must be installed for this figure factory.

Run the following commands to install the correct versions of the following modules:

```sh
pip3 install --user geopandas==0.3.0
pip3 install --user pyshp==1.2.10
pip3 install --user shapely==1.6.3
```

## What about Dash?

Opps! Don't forget to install Dash.

```
pip3 install --user dash==1.14.0
```

Everywhere in this apps that you see `fig.show()`, **you can display the same figure in a Dash application** by passing it to the figure argument of the `Graph` component from the built-in `dash_core_components` package like this:

```python
import plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
```
