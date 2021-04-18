from wsgiref.util import setup_testing_defaults
from views import Not_found_404_view


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = Not_found_404_view()
        request = {}
        # front controller
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        print(request)
        return [body.encode('utf-8')]