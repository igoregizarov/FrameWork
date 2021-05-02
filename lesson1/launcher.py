import time
from wsgiref.simple_server import make_server
from app import Application
from views import routes


# Front controllers

def now_time(request):
    request['time'] = time.ctime()


fronts = [now_time]

application = Application(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
