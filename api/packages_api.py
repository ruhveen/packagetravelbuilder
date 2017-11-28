import webapp2
import json
import logging
from google.appengine.ext import ndb
from helpers.serialize_helper import SerializeHelper
from helpers.base_handler import BaseHandler
from business_logic.package_builder import PackageBuilder


class PackagesAPI(BaseHandler):

    # /api/packages/new
    def post(self, action):
        if action == 'new':
            package = self.build_package()

            self.print_ndb_model(package)

    def build_package(self):

        args = {arg:self.request.get(arg) for arg in self.request.arguments()}
        return PackageBuilder.build(**args)


app = webapp2.WSGIApplication([
    ('/api/packages/(.*)', PackagesAPI)

], debug=True)