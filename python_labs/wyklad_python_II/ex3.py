#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

def replaceText(node, newText):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("node does not contain text")
    node.firstChild.replaceWholeText(newText)

DOMTree = xml.dom.minidom.parse("test1.xml")
collection = DOMTree.documentElement
movies = collection.getElementsByTagName("movie")
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print ("Title: %s" % movie.getAttribute("title"))
    type = movie.getElementsByTagName('type')[0]
    print ("Type: %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    replaceText(type, "type test")

file_handle = open("out.xml","wb") 
collection.writexml(file_handle) 
file_handle.close()