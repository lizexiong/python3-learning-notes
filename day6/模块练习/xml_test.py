





import xml.etree.ElementTree as ET

root = ET.Element('root')       # 创建根节点

class1 = ET.SubElement(root, 'class')  # root节点下创建clss元素的class1节点

student1 = ET.SubElement(class1, 'student')
student1.set('id', '101')
student1.set('name', '李泽雄')       # set方法在原有属性后加上新属性，或者修改同名属性
age1 = ET.SubElement(student1, 'age')
age1.text = '29岁'
sex1 = ET.SubElement(student1, 'sex')
sex1.text = '男'

student2 = ET.SubElement(class1, 'student')
student2.attrib = {'id': '102', 'name': '吴鑫哲'}  # attrib会完全替换原有属性
age2 = ET.SubElement(student2, 'age')
age2.text = '39岁'
sex2 = ET.SubElement(student2, 'sex')
sex2.text = '男'

class2 = ET.SubElement(root, 'class')

student3 = ET.SubElement(class2, 'student')
student3.attrib = {'id': '202', 'name': '刘稳'}
age3 = ET.SubElement(student3, 'age')
age3.text = '32岁'
sex3 = ET.SubElement(student3, 'sex')
sex3.text = '男'

tree = ET.ElementTree(root)      # 以root为根节点创建层级关系
tree.write('simple.xml', encoding="utf-8", xml_declaration=True)  # 写入文件声明
