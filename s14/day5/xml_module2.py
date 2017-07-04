import xml.etree.ElementTree as ET
import xml.dom.minidom
__author__ = "Steven Lee"

new_xml = ET.Element("data")
country = ET.SubElement(new_xml, "country", attrib={"name": "Liechtenstein"})
rank = ET.SubElement(country, "rank", attrib={"update": "yes"})
rank.text = '2'
gdppc = ET.SubElement(country, "gdppc")
gdppc.text = '141100'
neighbor = ET.SubElement(country, "neighbor", attrib={"direction": "E", "name": "Austria"})

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式
xml = xml.dom.minidom.parse("test.xml") # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
print(pretty_xml_as_string)

xml2 = xml.dom.minidom.toxml()
