import webapp2
import json
import logging
from helpers.serialize_helper import SerializeHelper
import traceback


class BaseHandler(webapp2.RequestHandler):

    def print_error(self, message='There was a problem'):
        message_object = {}
        message_object['result'] = None
        message_object['error'] = message
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'

        # For the dev environment
        self.response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        self.response.write(json.dumps(message_object))

    def handle_general_exception(self, err):
        logging.error('%s , %s ' % (err, traceback.format_exc()))
        self.print_error()

    def print_ndb_model(self, ndb_model):
        result = SerializeHelper.serialize_to_dict(ndb_model)
        self.print_object(result)

    def print_list_ndb_model(self, list_ndb_model):
        result = SerializeHelper.serialize_list_to_list_of_dict(list_ndb_model)
        self.print_object(result)

    def print_object(self, object):
        final_result = {}
        final_result['result'] = object
        final_result['error'] = None
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'

        # For the dev environment
        self.response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'

        self.response.write(json.dumps(final_result))

    # def validate_and_get_vendor(self, vendor_id_str):
    #     vendor_id = int(vendor_id_str)
    #     existing_vendor = Vendor.get_by_id(vendor_id)
    #     if not existing_vendor:
    #         self.print_error('Vendor was not found or not allowed')
    #
    #     return existing_vendor
