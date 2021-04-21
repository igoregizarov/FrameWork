from wsgiref.util import setup_testing_defaults
from views import Not_found_404_view
from request import PostRequests, GetRequests
import quopri


def decode_value(data):
    new_data = {}
    for k, v in data.items():
        val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val).decode('UTF-8')
        new_data[k] = val_decode_str
    return new_data


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'Пришёл post-запрос: {decode_value(data)}')

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Пришли GET-параметры: {request_params}')

        if path in self.routes:
            view = self.routes[path]
        else:
            view = Not_found_404_view()
        request = {}
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        print(request)
        return [body.encode('utf-8')]
