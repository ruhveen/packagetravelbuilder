from google.appengine.ext import ndb
from model.activity import Activity
from model.transfer import Transfer
from datetime import datetime
import random

class DayRoute(ndb.Model):

    activities_and_transfer = ndb.JsonProperty()
    date = ndb.DateProperty()
    budget = ndb.IntegerProperty()


    def build(self, categories):

        activities_and_transfer = []
        activities_and_transfer.append(self.create_random_activity(categories))
        activities_and_transfer.append(self.create_transfer())
        activities_and_transfer.append(self.create_random_activity(categories))
        activities_and_transfer.append(self.create_transfer())
        activities_and_transfer.append(self.create_random_activity(categories))


        self.activities_and_transfer =activities_and_transfer

    def create_random_activity(self, categories):

        randomized_categories = random.sample(set(categories),2)

        if 'museum' in randomized_categories:
            a = Activity(name='The famouse museum',category_ids=['museum'])

        elif 'food' in randomized_categories:
            a = Activity(name='The famous restaurnat',category_ids=['food','asianfood'])

        else:
            a = Activity(name='The famouse activity',category_ids=['laidback'])

        return a.to_dict()

    def create_transfer(self):

        t = Transfer(from_location='132131,421421',to_location='34234,2342',duration=30.5)
        t.is_transfer = True

        return t.to_dict()

    # def to_dict(self):
    #     result = super(DayRoute,self).to_dict()
    #
    #
    #     result['date'] = self.date.strftime("%Y-%m-%d")
    #     return result

