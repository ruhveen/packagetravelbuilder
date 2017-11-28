from google.appengine.ext import ndb
from model.day_route import DayRoute


class Package(ndb.Model):

    days = ndb.StructuredProperty(DayRoute, repeated=True)
    total_budget = ndb.IntegerProperty()


