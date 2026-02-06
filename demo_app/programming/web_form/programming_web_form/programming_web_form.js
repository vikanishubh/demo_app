frappe.ready(function () {

    frappe.web_form.on('enable', function (field, value) {
        if (value) {
            frappe.msgprint("Please fill all values carefully");
        }
    });

   
    frappe.web_form.on('dob', function (field, value) {
        if (value) {
            let dob = new Date(value);
            let today = new Date();

            let age = Math.floor(
                (today - dob) / (365.25 * 24 * 60 * 60 * 1000)
            );

            frappe.web_form.set_value('age', age);
        }
    });

    
    frappe.web_form.validate = () => {
        
        let mobileNum = frappe.web_form.get_value('mobile_no');
        let validateMobNum = /^[6-9]\d{9}$/;
        if (mobileNum && !validateMobNum.test(mobileNum)) {
            frappe.throw('Please enter a valid Mobile Number.');
            return false;
        }

       
        let email = frappe.web_form.get_value('email');
        let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email && !pattern.test(email)) {
            frappe.throw('Please enter a valid email address.');
            return false;
        }

        return true; 
    };

});
