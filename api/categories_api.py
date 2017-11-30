import webapp2
import json
import logging
from google.appengine.ext import ndb
from helpers.serialize_helper import SerializeHelper
from helpers.base_handler import BaseHandler

CATEGORIES = ['museum','asianfood','soccer','nightlife','beaches','laidback','art','vegan']

class CategoriesAPI(BaseHandler):


    def get(self):
        self.print_object(CATEGORIES)

app = webapp2.WSGIApplication([
    ('/api/categories', CategoriesAPI)

], debug=True)