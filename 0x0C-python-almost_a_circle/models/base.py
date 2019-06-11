#!/usr/bin/python3
""" Module base.py """
import json


class Base():
    """ New class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Passing to json string from python """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saving into a file .json """
        jsn_list = cls.to_json_string(list_objs)
        print(jsn_list)
        with open('{}.json'.format(cls), 'w') as myfile:
            json.dump(jsn_list, myfile)

    @staticmethod
    def from_json_string(json_string):
        """ From json string to python """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
