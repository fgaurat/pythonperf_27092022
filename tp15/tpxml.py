import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('country_data.xml')
    root = tree.getroot()
    print(root.tag)
    for child in root:
        print(child.tag, child.attrib)

if __name__ == '__main__':
    main()




# SAX
# DOM