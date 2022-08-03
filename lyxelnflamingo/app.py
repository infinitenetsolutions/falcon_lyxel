import falcon
from .resource import Resource
from .resource_list import ResourceList

app = application = falcon.App()
app.add_route('/api/insert', Resource())
app.add_route('/api/graph', ResourceList())
l;k`;lk;lkbcvn
