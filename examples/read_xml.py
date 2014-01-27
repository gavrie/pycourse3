from xml.etree import ElementTree
tree = ElementTree.parse("./companies-he.xml")
root = tree.getroot()

companies = root.find('companies')

for company in companies:
    name = company.find('name')
    print name.text
