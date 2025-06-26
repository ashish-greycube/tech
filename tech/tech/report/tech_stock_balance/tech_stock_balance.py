# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
import erpnext
from frappe import _
from erpnext.stock.report.stock_balance.stock_balance import execute as _execute
from erpnext.stock.report.stock_balance.stock_balance import StockBalanceReport 

def execute(filters=None):
	if not filters:
		filters = {}
	columns, data = [], []

	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	self = frappe._dict({
		'filters': filters
	})
	columns = StockBalanceReport.get_columns(self)

	columns.insert(1, {
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