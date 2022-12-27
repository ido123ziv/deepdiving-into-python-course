import xml.etree.ElementTree as ET

# Reading
tree = ET.parse('data.xml')

# getting the parent tag of
# the xml document
root = tree.getroot()

for child in root:
    print(child.tag)
    print("city: {}".format(child.find('address').attrib.get('city')))
    print("number: {}".format(child.find('address').find('no').text))

names = [child.find('name').text for child in root]
print(names)

# writing
data = ET.Element('Persons')
for name in names:
    elem1 = ET.SubElement(data, "person")
    s_elem1 = ET.SubElement(elem1, 'name')
    s_elem1.text = name
b_xml = ET.tostring(data)
with open("names.xml", "wb") as f:
    f.write(b_xml)
    