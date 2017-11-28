from google.appengine.ext import ndb
import json
from model.package import Package


class SerializeHelper(object):

    @staticmethod
    def serialize_to_dict(ndb_model_instance, exclude_properties=[]):
        result = ndb_model_instance.to_dict(exclude=exclude_properties)
        if ndb_model_instance.key:
            result['id'] = ndb_model_instance.key.id()

        if type(ndb_model_instance) is Package:
            for day in result['days']:
                day['date'] = day['date'].strftime("%Y-%m-%d")

        for property_name in ndb_model_instance._properties:

            # If it is a key property, we neet to fetch it from the DB
            # and set it in the dictionary to be returned
            if type(ndb_model_instance._properties[property_name]) == ndb.KeyProperty:
                if type(result[property_name]) == list:
                    list_of_fetched_ndb_entities = ndb.get_multi(result[property_name])
                    result[property_name] = SerializeHelper.serialize_list_to_list_of_dict(list_of_fetched_ndb_entities)
                else:
                    result[property_name] = result[property_name].id()

        return result

    @staticmethod
    def serialize_to_json(ndb_model_instance):
        return json.dumps(SerializeHelper.serialize_to_dict(ndb_model_instance))

    @staticmethod
    def serialize_list_to_list_of_dict(ndb_model_instances, exclude_properties=[]):
        result = []
        for instance in ndb_model_instances:
            instance_dict = SerializeHelper.serialize_to_dict(instance, exclude_properties)
            result.append(instance_dict)

        return result

    @staticmethod
    def deserialize_entity_from_str(str, ndb_model_class):
        return SerializeHelper.deserialize_entity_from_json_object(json.loads(str), ndb_model_class)

    @staticmethod
    def deserialize_entity_from_json_object(json_dictionary, ndb_model_class):
        if type(ndb_model_class) == str:
            ndb_model_class = eval(ndb_model_class)

        new_entity = ndb_model_class()

        for sent_property_name, sent_property_value in json_dictionary.iteritems():

            if sent_property_name == 'id':
                new_entity.key = ndb.Key(ndb_model_class,sent_property_value)

            elif sent_property_name in ndb_model_class._properties:

                value_to_set = sent_property_value
                if type(ndb_model_class._properties[sent_property_name]) == ndb.KeyProperty:
                    if type(sent_property_value) == list:
                        items = []

                        # If it is a key property,
                        # we need to create the related entity, and set the key property of the related entity
                        # in the main entity
                        for item_to_deserialize in sent_property_value:
                            related_entity = SerializeHelper.deserialize_entity_from_json_object(item_to_deserialize,
                                                                            ndb_model_class._properties[sent_property_name]._kind)

                            related_entity.put()
                            items.append(related_entity.key)
                        value_to_set = items
                    else:
                        value_to_set = SerializeHelper.deserialize_entity_from_json_object(sent_property_value,
                                                                            ndb_model_class._properties[sent_property_name]._kind)

                setattr(new_entity, sent_property_name, value_to_set)
            else:
                raise Exception("Unknown property sent: %s" % sent_property_name)

        return new_entity