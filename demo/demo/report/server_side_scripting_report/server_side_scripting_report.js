// Copyright (c) 2025, Dorcas and contributors
// For license information, please see license.txt

frappe.query_reports["Server-Side Scripting Report"] = {
  filters: [
    {
      fieldname: "first_name",
      fieldtype: "Data",
      label: "First Name",
    },
    {
      fieldname: "last_name",
      fieldtype: "Data",
      label: "Last Name",
    },
    {
      fieldname: "email",
      fieldtype: "Data",
      label: "Email",
    },
    {
      fieldname: "dob",
      fieldtype: "Date",
      label: "Date of birth",
    },
  ],
};
