import falcon

from .resource import Resource
from .resource_list import ResourceList


app = application = falcon.App()

data = Resource()
records = ResourceList()
app.add_route('/api/insert', data)
app.add_route('/api/graph', records)