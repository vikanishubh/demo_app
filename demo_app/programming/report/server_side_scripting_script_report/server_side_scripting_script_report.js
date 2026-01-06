// Copyright (c) 2026, Shubh and contributors
// For license information, please see license.txt

frappe.query_reports["server side scripting script report"] = {
	"filters": [
		{
			"fieldname":"name",
			"label":__("server side scripting"),
			"fieldtype":"Link",
			"options":"server side scripting"
		},
		{
			"fieldname":"age",
			"label":__("Age"),
			"fieldtype":"Data",
		},
		{
			"fieldname":"dob",
			"label":__("D.O.B"),
			"fieldtype":"Date",
		}

	]
};
