from google.appengine.ext import ndb
from model.address import Address


class Activity(ndb.Model):
    name = ndb.StringProperty(required=True)
    category_id = ndb.StringProperty()
    description = ndb.StringProperty(required=True)
    duration = ndb.FloatProperty()
    price = ndb.IntegerProperty()
    address = ndb.StructuredProperty(Address)
    is_transfering = ndb.BooleanProperty()

