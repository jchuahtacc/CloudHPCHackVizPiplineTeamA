from werkzeug.middleware.dispatcher import DispatcherMiddleware
from gallery import app
from loader import get_dash_app_routes
from session_middleware import SessionMiddleware
import os

routes = get_dash_app_routes()

SESSION_VALUE = os.environ.get('GALLERY_SESSION_NAME', None)
TOKEN = os.environ.get('GALLERY_SESSION_TOKEN', None)

server = DispatcherMiddleware(app.server, routes)

if SESSION_VALUE and TOKEN:
    server = SessionMiddleware(server)