from google.appengine.ext import ndb
from model.activity import Activity
from datetime import datetime
import random

class DayRoute(ndb.Model):

    activities_and_transfer = ndb.JsonProperty()
    date = ndb.DateProperty()
    budget = ndb.IntegerProperty()


    def build(self, categories):

        activities_and_transfer = []
        activities_and_transfer.append(Activity(name='Musesom%s' % random.randint(1,100)).to_dict())
        activities_and_transfer.append(Activity(name='Musesom%s' % random.randint(1,100)).to_dict())
        activities_and_transfer.append(Activity(name='Musesom%s' % random.randint(1,100)).to_dict())
        activities_and_transfer.append(Activity(name='Musesom%s' % random.randint(1,100)).to_dict())

        self.activities_and_transfer =activities_and_transfer

    # def to_dict(self):
    #     result = super(DayRoute,self).to_dict()
    #
    #
    #     result['date'] = self.date.strftime("%Y-%m-%d")
    #     return result

