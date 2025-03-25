# Copyright (c) 2025, Dorcas and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
 
	columns = get_columns()
	cs_data = get_data(filters)
 
	if not cs_data:
		frappe.msgprint("No data found", alert=True)
		return columns, data
	else:
		data = []
		for d in cs_data:
			row = frappe._dict({
				"first_name": d.first_name,
				"last_name": d.last_name,
				"email": d.email
			})
			data.append(row)
  
 
	return columns, data

 

def get_columns():
  return [
		{
			"fieldname": "first_name",
			"label": "First Name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"fieldname": "last_name",
			"label": "Last Name",
			"fieldtype": "Data",
			"width": 120
		},
    {
			"fieldname": "email",
			"label": "Email",
			"fieldtype": "Data",	
			"width": 120
		}
	]
  
def get_data(filters):
  conditions = get_conditions(filters)
  data = frappe.get_all("Server-Side Scripting", fields=["first_name", "last_name", "email"], filters=conditions)
  return data


def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value