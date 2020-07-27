
from werkzeug.wrappers import Request, Response, ResponseStream
from werkzeug.utils import cached_property
from werkzeug.exceptions import Unauthorized
import os

SESSION_VALUE = os.environ.get('GALLERY_SESSION_NAME', 'session')
TOKEN = os.environ.get('GALLERY_SESSION_TOKEN', 'abcde')

class SessionMiddleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        # Look for a session with this instance of the Dash server
        if request.cookies.get('session', None) == SESSION_VALUE:
            return self.app(environ, start_response)

        # Look for a token in browser arguments
        if request.args.get('token', None) == TOKEN:
            # Session helper function
            def session_start_response(status, headers, exc_info=None):
                headers.append(('Set-cookie', 'session={}'.format(SESSION_VALUE)))
                return start_response(status, headers, exc_info)
            
            return self.app(environ, session_start_response)

        # Unauthorized response helper function
        def unauthorized_response(status, headers, exc_info=None):
            return start_response("401 Unauthorized", headers, exc_info)

        # If neither a session cookie nor a token were found, return 401 Unauthorized
        return Unauthorized()(environ, unauthorized_response)