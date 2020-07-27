import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import plotly
import plotly.express as px
import pathlib
import os
import importlib

################################################################################
##                                                                            ##
##  Devops                                                                    ##
##                                                                            ##
################################################################################

# Create a path object for './data'
DATA_PATH = pathlib.Path(__file__).parent.joinpath("data") 
ASSETS_PATH = pathlib.Path(__file__).parent.joinpath("assets")
REQUESTS_PATHNAME_PREFIX = os.environ.get("REQUESTS_PATHNAME_PREFIX", "/")

if __name__ == "__main__":
    # If running in debug mode independent of rolodex start with no options
    app = dash.Dash(
        __name__,
        assets_folder=ASSETS_PATH
    )
else:
    # If served from rolodex/gunicorn, change options based on package name
    package_tokens = __package__.split('.')
    if len(package_tokens) > 1:
        REQUESTS_PATHNAME_PREFIX += "{}/".format(package_tokens[-1])

    app = dash.Dash(
        __name__,
        assets_folder=ASSETS_PATH,
        requests_pathname_prefix=REQUESTS_PATHNAME_PREFIX,
    )

if __package__ is None or len(__package__) == 0:
    # Local imports
    # import mymodule
    pass
else:
    # Local imports during production
    # mymodule = importlib.import_module('.mymodule', package=__package__)
    pass

server = app.server

app.layout = html.Div("A Dummy Hello World Dash Application")

if __name__ == '__main__':
    app.run_server(debug=True)
else:
    server = app.server
