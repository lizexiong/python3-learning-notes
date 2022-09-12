




import xml.etree.ElementTree as ET

tree = ET.parse('simple.xml')

root = tree.getroot()                   # 查找根节点
print(root.tag)                         # 结果：root

elem1 = root.find('class')              # 绝对路径不包括root,只能搜索到第一个符合条件的节点
print(elem1.tag)                        # 结果：class
print(elem1.attrib)                     # 结果：{}
print(elem1.text)                       # 结果： None
elem2 = root.find('class/student')      # 绝对路径用/分割,只能搜索到第一个符合条件的节点
print(elem2.tag)                        # 结果：student
print(elem2.attrib)                     # 结果：{'id': '101', 'name': '李泽雄'}
print(elem2.text)                       # 结果：None
elem3 = elem1.find('student/age')       # 绝对路径不包括elem1,只能搜索到第一个符合条件的节点
print(elem3.tag)                        # 结果：age
print(elem3.attrib)                     # 结果：{}
print(elem3.text)                       # 结果：29岁



import xml.etree.ElementTree as ET

tree = ET.parse('simple.xml')
root = tree.getroot()
elem1 = root.findall('class')         # 返回2个class节点的列表
elem2 = elem1[0].findall('student')   # 列表可以切片
for e in elem2:                       # 列表可以遍历
    print(e.attrib)


import xml.etree.ElementTree as ET

tree = ET.parse('simple.xml')
root = tree.getroot()
elem1 = root.iter('age')
for e in elem1:
    print(e.text)


import xml.etree.ElementTree as ET

tree = ET.parse('simple.xml')
root = tree.getroot()
elem1 = root.findall('class/student')
for e in elem1:
    print(ET.tostring(e, encoding="unicode"))
