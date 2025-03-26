frappe.pages["scripting-page"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "Server Scripting",
    single_column: true,
  });

  page.set_title("My Page");

  // page.set_indicator("Done", "green");
  // page.set_indicator("In Progress", "orange");
  // page.set_indicator("Not Started", "red");
  page.set_indicator("Open", "blue");

  page.set_primary_action("Click Me", () => frappe.msgprint("Hello World"));
  page.set_secondary_action("Refresh", () => frappe.msgprint("Page Refreshed"));

  page.add_menu_item("Item 1", () => frappe.msgprint("Item 1 Clicked"));

  page.add_action_item("Delete", () => frappe.msgprint("Delete Clicked"));

  let field = page.add_field({
    label: "Status",
    fieldtype: "Select",
    fieldname: "status",
    options: ["Open", "Closed", "Cancelled"],
    change: () => frappe.msgprint(field.get_value()),
  });

  // $(frappe.render_template("scripting_page", {})).appendTo(page.body);

  $(
    frappe.render_template("scripting_page", {
      data: "Hello World",
    })
  ).appendTo(page.body);
};
