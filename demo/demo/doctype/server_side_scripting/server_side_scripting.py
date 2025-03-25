# Copyright (c) 2025, Dorcas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document 

class ServerSideScripting(Document):
    def onload(self):
        self.check_if_exists()
        self.count_records() 
        self.get_records_sql()  
 
    def validate(self):    
        self.get_value()                       
        self.delete_document()        
         
    def check_if_exists(self):  
        result = frappe.db.exists("Server-Side Scripting", self.name) 

        if result:
            frappe.msgprint("Record exists.", alert=True)  
        else:      
            frappe.msgprint("Record does not exist.", alert=True)   
            
    def count_records(self):
        count = frappe.db.count("Server-Side Scripting") 
        frappe.msgprint(f"Total records {count}") 
    
    def get_records_sql(self): 
        result = frappe.db.sql("SELECT first_name, last_name FROM `tabServer-Side Scripting`")
        
        for row in result:
            frappe.msgprint(f"First Name: {row[0]} Last Name: {row[1]}")
        
    def get_value(self):
        result = frappe.db.get_value("Server-Side Scripting", self.name, ['first_name', 'last_name'], as_dict=True)

        if result:  
            first_name = result.get("first_name", "")
            last_name = result.get("last_name", "")

            full_name = f"{first_name} {last_name}"
            frappe.msgprint(f"Saved: {full_name}")

            # Corrected set_value() usage
            frappe.db.set_value("Server-Side Scripting", self.name, "full_name", full_name)
        else:
            frappe.msgprint("No record found or missing fields.", alert=True)

    def create_new_document(self):
        doc = frappe.new_doc("Server-Side Scripting")
        doc.first_name = "John" 
        doc.last_name = "Doe" 
        doc.age = 30 
        doc.dob = "1995-01-01"  
        doc.append('dependents', {                              
            'full_name': 'Jane Doe',
            'relation': 'Spouse',  
            'age': 25
        })  
        
        frappe.msgprint("New document created.", alert=True)
        doc.insert()  
    
    def delete_document(self):
        result = frappe.delete_doc("Server-Side Scripting", 'SS-00009') 
         
        if result:  
            frappe.msgprint("Document deleted.", alert=True)
        else:
            frappe.msgprint("Document to delete not found.", alert=True
        )
        
    def set_value(self): 
        frappe.db.set_value("Server-Side Scripting", self.name, "age", "25") 
    