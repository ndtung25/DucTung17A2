from xml.dom import minidom

doc = minidom.parse("sample.xml")

company_name = doc.getElementsByTagName("name")[0].firstChild.data
print(f"Company Name: {company_name}")

staffs = doc.getElementsByTagName("staff")

for staff in staffs:
    staff_id = staff.getAttribute("id")
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    
    print(f"Staff ID: {staff_id}")
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print("-" * 20)