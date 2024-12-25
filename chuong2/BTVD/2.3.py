import xml.dom.minidom

def parse_xml(file_name):
    doc = xml.dom.minidom.parse(file_name)
    
    company_name = doc.getElementsByTagName("name")[0].firstChild.nodeValue
    print(f"Company Name: {company_name}")
    
    staff_list = doc.getElementsByTagName("staff")
    print("\nStaff Information:")
    
    for staff in staff_list:
        staff_id = staff.getAttribute("id")
        staff_name = staff.getElementsByTagName("name")[0].firstChild.nodeValue
        staff_salary = staff.getElementsByTagName("salary")[0].firstChild.nodeValue
        print(f"ID: {staff_id}, Name: {staff_name}, Salary: {staff_salary}")

if __name__ == "__main__":
    parse_xml("sample.xml")