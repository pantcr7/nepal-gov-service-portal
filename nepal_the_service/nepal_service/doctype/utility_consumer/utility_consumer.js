// Copyright (c) 2024, PP and contributors
// For license information, please see license.txt

frappe.ui.form.on("Utility Consumer", {
	refresh(frm) {
        if (frm.doc.__islocal) {
            frm.set_df_property("user_details_section", "hidden", true);
        }
        else {
            if (frm.doc.user_id) {
                frm.set_df_property("create_user", "hidden", true);
            }
            frm.set_df_property("user_details_section", "hidden", false);

        }

	},
    user_id:function(frm){
        if (frm.doc.user_id) {
          frm.set_df_property("create_user", "hidden", true);
        }
        else {
            frm.set_df_property("create_user", "hidden", false);
        }

    },
    create_user: function(frm) {
		if (!frm.doc.email) {
			frappe.throw(__("Please enter Preferred Contact Email"));
		}
		frappe.call({
			method: "nepal_the_service.nepal_service.doctype.utility_consumer.utility_consumer.create_user",
			args: {
				consumer: frm.doc.name,
				email: frm.doc.email
			},
			freeze: true,
			freeze_message: __("Creating User..."),
			callback: function (r) {
                frm.set_df_property("create_user", "hidden", true);
				frm.reload_doc();
			}
		});
	}


    
});
