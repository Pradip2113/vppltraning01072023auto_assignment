// Copyright (c) 2023, Abhishek Chougule and contributors
// For license information, please see license.txt

frappe.ui.form.on('Auto Shift Assignment', {

    on_submit: function(frm) {
		
        frm.call({
			
            method:'auto_save_assignment',
            doc: frm.doc,
            
        });
        
    }
});

