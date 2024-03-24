from xml.etree.ElementTree import Element, ElementTree
root = Element("Acordeon")
todeschinni = Element("Todeschinni")
scandalli = Element("Scandalli", cor="preta", modelo="120 baixos")
maestrina = Element("Maestrina")
root.append(todeschinni)
root.append(scandalli)
root.append(maestrina)
ElementTree(root).write("sanfona.xml")