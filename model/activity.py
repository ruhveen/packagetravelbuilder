from google.appengine.ext import ndb
from model.address import Address


class Activity(ndb.Model):
    name = ndb.StringProperty(required=True)
    category_ids = ndb.StringProperty(repeated=True)
    description = ndb.StringProperty(required=True)
    duration = ndb.FloatProperty()
    price = ndb.IntegerProperty()
    address = ndb.StructuredProperty(Address)

