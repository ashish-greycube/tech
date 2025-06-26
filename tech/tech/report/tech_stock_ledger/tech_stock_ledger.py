# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

import erpnext
from erpnext.stock.report.stock_ledger.stock_ledger import execute as _execute
from erpnext.stock.report.stock_ledger.stock_ledger import get_columns as _get_columns

def execute(filters=None):
	if not filters:
		filters = {}
	columns, data = [], []
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	columns = _get_columns(filters)
	columns.insert(2, {
		'fieldname' : 'barcode',
		'fieldtype' : 'Data',
		'label' : _('Barcode'),
		'width' : 150
	})
	return columns

def get_data(filters):
	data = _execute(filters)
	if len(data)>0:
		for d in data[1]:
			item = d.item_code
			d['barcode'] = frappe.db.get_value('Item', {'name': item}, 'custom_barcode')
		return data[1]