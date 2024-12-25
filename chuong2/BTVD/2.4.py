import xml.dom.minidom

def print_element_names(file_name):
    doc = xml.dom.minidom.parse(file_name)
    
    all_elements = doc.getElementsByTagName("*")
    
    print("Tên các phần tử trong tệp XML:")
    for element in all_elements:
        print(element.tagName)

if __name__ == "__main__":
    print_element_names("sample.xml")