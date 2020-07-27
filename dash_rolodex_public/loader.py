import pkgutil
import importlib
import shutil
import os
import traceback
import pathlib
import json

def get_dash_app_routes():
    routes = { }
    for p in pkgutil.iter_modules(path=['./apps']):
        app = importlib.import_module('apps.{}.app'.format(p.name))
        routes['/{}'.format(p.name)] = app.app.server
    return routes

def thumbnail_path(dash_name, thumbnail_path):
    return '{}_{}'.format(
        dash_name,
        thumbnail_path
    )