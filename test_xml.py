#!/usr/bin/python
# -*- coding=utf-8 -*-
from xml.etree.ElementTree import ElementTree,Element,SubElement
import os
import time
from xml.dom import minidom
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def create_node(tag, property_map):
    element = Element(tag, property_map)
    return element
def add_child_node(nodes, element):
    for node in nodes:
        node.append(element)
def make_xml(path):
    if not os.path.exists(path):
        root = Element('pictures')
        tree = ElementTree(root)
        tree.write(path, encoding="utf-8", xml_declaration=True)
def write_xml(path, time_0, output_class, output_index, picture_path, model):
    if os.path.exists(path):
        print("a")
        tree = ElementTree()
        tree.parse(path)
        root = tree.getroot()
        print(str(root))
        son=SubElement(root, 'picture',
                       {"time": time_0, "content": output_class, "remarks": output_index, "picture": picture_path, "model": model})
        # a = create_node("video", {"time": time, "terminal": camera, "content": "攀爬围墙", "remarks": "", "file": video_path})
        # add_child_node(nodes, a)
        son.tail = '\n'
        tree.write(path, encoding="utf-8", xml_declaration=True)

    else:
        print('b')
        root = Element('pictures')
        son = SubElement(root,'picture',{"time": time_0, "content": output_class, "remarks": output_index, "video": picture_path, "model": model})
        son.tail = '\n'
        tree = ElementTree(root)
        tree.write(path,encoding="utf-8", xml_declaration=True)


# make_xml('./test.xml')
# write_xml('./test.xml','time','output_class','output_index','./suyw/sy','face1')
# write_xml('./test.xml','time','output_class','output_index','./suyw/sy','face2')
# write_xml('./test.xml','time','output_class','output_index','./suyw/sy','face3')