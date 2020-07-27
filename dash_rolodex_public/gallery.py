from flask import Flask, request
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pathlib
import os
from flask import request, Flask
from loader import thumbnail_path

#####################################################################################################################
##                                                                                                                 ##
##  Helper function to get an Agave client.                                                                        ##
##                                                                                                                 ##
#####################################################################################################################

# Create a path object for './data'
DATA_PATH = pathlib.Path(__file__).parent.joinpath("data") 
ASSETS_PATH = pathlib.Path(__file__).parent.joinpath("assets")
REQUESTS_PATHNAME_PREFIX = os.environ.get("REQUESTS_PATHNAME_PREFIX", "/")

print("Reading dashmeta.json...")
try:
    with open("dashmeta.json", "r") as dash_meta_file:
        dash_meta = json.load(dash_meta_file)
except:
    print("Unable to open dashmeta.json")
    dash_meta = { }

print("Reading gallerymeta.json...")
with open("gallerymeta.json", "r") as gallery_meta_file:
    gallery_meta = json.load(gallery_meta_file)

print("Assets at {}".format(ASSETS_PATH))
app = dash.Dash(
    __name__,
    assets_folder=ASSETS_PATH,
    requests_pathname_prefix=REQUESTS_PATHNAME_PREFIX
)
app.config.suppress_callback_exceptions = True

server = app.server

def create_dash_launcher(dash_name):
    """
    Generate an individual Dash launcher element. This element
    exposes the "description", "thumbnail" and "name" elements of 
    a dash app's metadata and launches them in a new browser window
    """
    dash = dash_meta[dash_name]
    return html.Figure(
        className="gallery__item",
        children=[
            html.H2(
                html.A(
                    dash["name"],
                    className="gallery__item-link u-stretched-link",
                    target="_blank",
                    href="{}/".format(dash_name)
                ),
                className="gallery__item-title"
            ),
            html.Img(
                src=app.get_asset_url(thumbnail_path(dash_name, dash["thumbnail"])),
                className="gallery__item-figure"
            ),
            html.Figcaption(
                dash["description"],
                className="gallery__item-desc"
            )
        ]
    )

def create_header():
    """
    Create the gallery's header element. This uses the "name"
    metadata from gallerymetadata.json
    """
    return html.H1(
        gallery_meta["name"],
        className="gallery__title"
    )

def create_gallery():
    """
    Create a gallery container with dash launchers
    """
    launchers = [ create_dash_launcher(dash_name) for dash_name in dash_meta.keys() ]
    return html.Div(
        id="apps",
        className="dash-gallery",
        children=launchers
    )

def serve_layout():
    """
    Assemble the global layout and return it
    """
    return html.Div(
        children=[
            create_header(),
            create_gallery()
        ]
    )

app.layout = serve_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
