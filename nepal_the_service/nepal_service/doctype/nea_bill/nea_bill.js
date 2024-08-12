// Copyright (c) 2024, PP and contributors
// For license information, please see license.txt

frappe.ui.form.on("NEA Bill", {
	refresh(frm) {
        if(frm.doc.status == "Paid") {
            frm.disable_form();
        }
	},
    consumer_name: function(frm) {
        frappe.call({
            method:"frappe.client.get",
            args: {
                doctype: "Utility Consumer",
                filters: {
                    name: frm.doc.consumer_name
                },
              
            },
            callback: function(data) {
                frm.set_value("consumer_address", data.message.address);
                frm.set_value("consumer_phone", data.message.phone);
                frm.set_value("consumer_id", data.message.nea_consumer_id);
            }
        });
    },
    usage: function(frm) {
        frm.set_value("amount", frm.doc.usage * frm.doc.rate_per_unit);
    },
    create_button: function(frm) {
    }


});
