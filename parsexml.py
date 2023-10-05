"""
Cisco devops class assignment using vulnerable XML parsing code that
can allow for injection of malicious xml. DO NOT USE THIS IN PRODUCTION
see python docs for updated xml parsing. Using outdated module as per assignment requirements.
"""

import xml.etree.ElementTree as ET
import re

tree = ET.parse('myfile.xml')
root = tree.getroot()
# most of this code is pasted from assignment
# var xml changed to tree as per python docs to eliminate confusion with xml.etree.ElementTree

ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))
#  using regex to search xml data

print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))
# .format(defop.text) takes the object stored at defop and
# formats it into human-readable text, this is based on C code
# an f string would just return the element and memory location

