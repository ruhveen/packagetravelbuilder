from google.appengine.ext import ndb


class Address(ndb.Model):
    street = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zip = ndb.StringProperty()
    country = ndb.StringProperty()