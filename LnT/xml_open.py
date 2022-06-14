import lxml
from lxml import etree
xml_list = []
with open('Lnt_Project/ACORD_XML_For_SubmittionToCarrier.xml', 'r') as f:
    root = etree.parse(f)
    for e in root.iter():
        path = root.getelementpath(e)
        print(path)

