import xml.etree.ElementTree as ET
tree=ET.parse('country_data.xml')
root=tree.getroot()
#root has tag and a dictionary of attrib
print root.tag
print root.attrib
#root->child node
for child in root:
	print child.tag,child.attrib
	
#specific child node by index
print root[0][1].text

#iterate recursively over all sub-tree below it
for neighbor in root.iter('neighbor'):
	print neighbor.attrib
	
#findall
for country in root.findall('country'):
	rank=country.find('rank').text
	name=country.get('name')
	print name,rank
