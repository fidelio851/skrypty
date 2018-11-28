#!/usr/bin/python

# from xml.dom.minidom import parse
# dom = parse("xmlfile.xml")
# for node in dom.getElementsByTagName('to'):  # visit every node <bar />
# 	print node.toxml()
#     replaceText(node, "Hello World")
#     print node.toxml()

from xml.etree import ElementTree as et
tree = et.parse('xmlfile.xml')
tree.find('to').text = 'too'
tree.write('xmlfile.xml')