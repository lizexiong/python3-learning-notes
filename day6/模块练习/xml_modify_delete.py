





import xml.etree.ElementTree as ET

tree = ET.parse('simple.xml')
root = tree.getroot()
elem1 = root.findall('class')
for e in elem1:
    e.tag = 'grade'    # 将class元素改名为grade元素

tree.write('simple.xml')
