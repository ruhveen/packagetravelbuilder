from google.appengine.ext import ndb
from model.address import Address


class Transfer(ndb.Model):
    name = ndb.StringProperty(required=True)
    is_transfer = ndb.BooleanProperty()
    from_location = ndb.StringProperty()
    to_location = ndb.StringProperty()
    duration = ndb.FloatProperty()

