#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        jsn_list = cls.to_json_string(list_objs)
        print(jsn_list)
        with open('{}.json'.format(cls), 'w') as myfile:
            return json.dump(jsn_list, myfile)
