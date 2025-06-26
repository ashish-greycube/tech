import frappe

def set_barcode_on_save(self, method=None):
    item = self.item_code
    if len(self.barcodes) > 0:
        barcode = self.barcodes[0].barcode
        self.custom_barcode = barcode   
