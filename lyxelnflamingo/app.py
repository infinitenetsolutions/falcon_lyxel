import falcon

from .resource import Resource


app = application = falcon.App()

data = Resource()
app.add_route('/api/insert', data)