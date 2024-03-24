from xml.etree.ElementTree import ElementTree
tree=ElementTree(file="Sanfonas.xml")
root=tree.getroot()
scandalli=root.find("Scandalli")
print(scandalli.tag)
print(scandalli.attrib)
root.remove(root.find("Todeschinni"))
