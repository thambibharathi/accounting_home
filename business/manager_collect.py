from business.manager_models import *
from business.managerapi import manager_browser, manager_object, USER_NAME,PASSWORD,ROOT_URL

m=manager_object(ROOT_URL,USER_NAME,business='Demo Company Indian GST')

sinvoices=m.get_sales_invoices()
tcodes=m.get_taxCodes()
customers=m.get_customers()
#suppliers=m.get_suppliers()

sinvoice_list=[]
for sinvoice in sinvoices:
  sinvoice_list.append(sinvoices[sinvoice])
  
