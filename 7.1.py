import xml.etree.ElementTree
import copy

class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    xml_d = xml.etree.ElementTree.parse('items.xml')
    root = xml_d.getroot()
    prototype = Prototype()
    prototype.register_object('items.xml', xml_d)
    b = prototype.clone('items.xml')

main()