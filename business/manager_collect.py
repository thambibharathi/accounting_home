from business.managerapi import manager_browser, manager_object, USER_NAME,PASSWORD,ROOT_URL
from business.manager_models import *

m=manager_object(ROOT_URL,USER_NAME,business='Demo Company Indian GST')

sinvoices=m.get_sales_invoices()
tcodes=m.get_taxCodes()
customers=m.get_customers()
#suppliers=m.get_suppliers()

sinvli=[] # List of sales invoice objects
for sinvoice in sinvoices:
  sinvli.append(SalesInvoice(sinvoices[sinvoice]))
  
cli=[]  # List of customer objects
for customer in customers:
  cli.append(CustomerDetails(customers[customer]))
  
taxli=[]
for tax in tcodes:
  taxli.append(TaxCode(tcodes[tax],tax))
  
            
    
