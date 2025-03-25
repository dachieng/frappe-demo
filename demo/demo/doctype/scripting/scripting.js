// Copyright (c) 2025, Dorcas and contributors
// For license information, please see license.txt

frappe.ui.form.on("Scripting", {
  refresh(frm) {
    // frappe.msgprint("Hello World");
    // frappe.throw('Error message goes here')

    frm.add_custom_button("Click Me", () => {
      frappe.msgprint("Hello World");
    });
  },
  onload(frm) {
    frappe.msgprint("The form has been loaded");
  },
  after_save(frm) {
    frappe.msgprint(
      `The full name is ${frm.doc.full_name} and the age is ${frm.doc.age}`
    );

    for (let row of frm.doc.dependants) {
      frappe.msgprint(`The  name of the dependant is ${row.name}`);
    }
  },
  validate(frm) {
    if (frm.doc.first_name && frm.doc.last_name) {
      frm.set_value("full_name", `${frm.doc.first_name} ${frm.doc.last_name}`);
    }

    if (frm.doc.dob) {
      const dob = new Date(frm.doc.dob);
      const today = new Date();
      let age = today.getFullYear() - dob.getFullYear();
      const month = today.getMonth() - dob.getMonth();

      if (month < 0 || (month === 0 && today.getDate() < dob.getDate())) {
        age--;
      }

      frm.set_value("age", age);
    }
  },
  // enable: function(frm) {
  //   if (frm.doc.enable) {
  //     frm.set_df_property('first_name', 'reqd', 1);
  //   }
  // }
});
