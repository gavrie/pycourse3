from xml.etree import ElementTree
tree=ElementTree.parse('./country_data.xml')
root=tree.getroot()
liechtenstein = root.find('country')
liechtenstein.attrib['name'] = 'Moshe'
liechtenstein.tag = 'whatever'
year = liechtenstein.find('year')
year.text = '2014'
tree.write('updated.xml')
