import xml.etree.cElementTree as ET
import sys
def newid():
    maxid = 0
    for contact in root.findall('contact'):
        id= int(contact.find('id').text)
        if id>maxid:
            maxid=id
            return maxid+1
def createStudent():
        #add a record-but we would need to check for duplicates first
        #ask the user for the student email address to search for
    email =input("Enter the Email address of the student you want to search for: ")    
        #exists=recordExists(email)
    exists=False
    if exists==False:
            
            #gt a new id
        nid=newid()

            #get the field values from the user
        print("Create a record")
        name=input("Name:")
        address=input("Address:")
        age=input("Age:")
        email=input("Email:")
        phone=input("Phone:")

            #create a contact element at root level
        newrecord = ET.SubElement(root, "contact",id=str(nid))

            #add the fields into out new record
        ET.SubElement(newrecord, "id", name="id").text = str(nid)
        ET.SubElement(newrecord, "name", name="name").text = name
        ET.SubElement(newrecord, "address", name="address").text = address
        ET.SubElement(newrecord, "phone", name="phone").text = phone
        ET.SubElement(newrecord, "email", name="email").text = email
        ET.SubElement(newrecord, "age", name="age").text = age

            #finally save the update
        ntree.write("students.xml")    

    else:
        print("--------------------------------------------")
        print("Record already exists")
        print("--------------------------------------------")
try:
    ntree = ET.parse('students.xml')
    root = ntree.getroot()
    createStudent()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise            