import datetime
from wsgiref.simple_server import make_server
from app import Application
from url import routes


# Front controllers

def now_time(request):
    request['time'] = datetime.datetime.now()


fronts = [now_time]

application = Application(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
