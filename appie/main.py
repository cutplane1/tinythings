import re

class Appie:
    def __init__(self):
        self.routes = []
    
    def add(self, verb, path, handler):
        pattern = re.sub(r'<(\w+)>', r'(?P<\1>[^/]+)', path)
        self.routes.append((verb, re.compile(f'^{pattern}$'), handler))
    
    def dispatch(self, verb, path):
        for http_verb, pattern, handler in self.routes:
            match = pattern.match(path)
            if match and verb == http_verb:
                return handler(**match.groupdict())
        raise Exception(404)

    def get(self, path):
        def wrapper(handler):
            self.add('GET', path, handler)
            return handler
        return wrapper
    
    def post(self, path):
        def wrapper(handler):
            self.add('POST', path, handler)
            return handler
        return wrapper
    
    def put(self, path):
        def wrapper(handler):
            self.add('PUT', path, handler)
            return handler
        return wrapper
    
    def delete(self, path):
        def wrapper(handler):
            self.add('DELETE', path, handler)
            return handler
        return wrapper
    
    def patch(self, path):
        def wrapper(handler):
            self.add('PATCH', path, handler)
            return handler
        return wrapper
    
    def options(self, path):
        def wrapper(handler):
            self.add('OPTIONS', path, handler)
            return handler
        return wrapper
    
    def wsgi(self, environ, start_response):
        verb = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        try:
            d = self.dispatch(verb, path)
        except Exception as e:
            d = str(e)
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [d.encode('utf-8')]
        
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [d.encode('utf-8')]

    def dev_server(self, host='127.0.0.1', port=8000):
        print(f'Serving on http://{host}:{port}')
        from wsgiref.simple_server import make_server
        httpd = make_server(host, port, self.wsgi)
        httpd.serve_forever()



a = Appie()

@a.get('/')
def index():
    return 'index page'

a.dev_server()