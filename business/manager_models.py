class BusinessDetails:
  def __init__(self):
    self.tradingName=tradingName
    self.contactDetails=contactDetails
    self.businessIdentifier=businessIdentifier
    
  def __str__(self):
    return self.tradingName
    
class CustomerDetails:
  def __init__(self,customer={}):
    customer=customer
    self.name=customer.get('Name',None)
    self.billingAddress=customer.get('BillingAddress',None)
    self.email=customer.get('Email',None)
    self.businessIdentifier=customer.get('BusinessIdentifier',None)
    self.code=customer.get('Code',None)
    self.startingBalanceType=customer.get('StartingBalanceType',None)
    self.telephone=customer.get('Telephone',None)
    self.fax=customer.get('Fax',None)
    self.mobile=customer.get('Mobile',None)
    self.notes=customer.get('Notes',None)
    self.customFields=customer.get('CustomFields',None)
    self.creditLimit=customer.get('CreditLimit',None)
    self.startingBalanceType=customer.get('StartingBalanceType',None)
    
  def __str__(self):
    return self.name
 
class SupplierDetails:
  def __init__(self,supplier={}):
    supplier=supplier
    self.name=supplier.get('Name',None)
    self.email=supplier.get('Email',None)
    self.telephone=supplier.get('Telephone',None)
    self.fax=supplier.get('Fax',None)
    self.mobile=supplier.get('Mobile',None)
    self.notes=supplier.get('Notes',None)
    self.address=supplier.get('Address',None)
    self.customFields=supplier.get('CustomFields',None)
    self.code=supplier.get('Code',None)
    self.creditLimit=supplier.get('CreditLimit',None)
    
  def __str__(self):
    return self.name

class SalesInvoice:
   def __init__(self,salesinv={} ):
      salesinv=salesinv
      self.issueDate=salesinv.get('IssueDate',None)
      self.reference=salesinv.get('Reference',None)
      self.to=salesinv.get('To',None)
      self.billingAddress=salesinv.get('BillingAddress',None)
      self.lines=salesinv.get('Lines',None)
      self.dueDate=salesinv.get('DueDate',None)
      self.discount=salesinv.get('Discount',None)
      self.amountsIncludeTax=salesinv.get('AmountsIncludeTax',None)
      self.roundingMethod=salesinv.get('RoundingMethod',None)
      self.dueDateType=salesinv.get('DueDateType',None)
      self.dueDateDays=salesinv.get('DueDateDays',None)
      self.latePaymentFees=salesinv.get('LatePaymentFees',None)
      self.latePaymentFeesPercentage=salesinv.get('LatePaymentFeesPercentage',None)
      self.rounding=salesinv.get('Rounding',None)
      
   def __str__(self):
      return self.reference
   
   @property 
   def lines_list(self):
      lines_list=[]
      for line in self.lines:
        lines_list.append(SalesInvLine(line))
      return lines_list
   

class SalesInvLine:
   def __init__(self,line,amountsIncludeTax=None):
      self.taxcode=taxcode #contains all tax codes
      self.amountsIncludeTax=amountsIncludeTax
      self.description=line.get('Description',None)
      self.account=line.get('Account',None)
      self.taxCode=line.get('TaxCode',None)
      self.qty=line.get('Qty',None)
      self.item=line.get('Item',None)
      self.amount=line.get('Amount',None)
      self.discount=line.get('Discount',None)
      self.trackingCode=line.get('TrackingCode',None)
      self.customFields=line.get('CustomFields',None)
      
   @property
   def amt_aft_discount(self):
      if self.discount is not None:
        return int(self.amount) -  ((int(self.amount)*int(self.discount))/100 )
      else :
        return int(self.amount)
   
   def get_tax_obj(self):
       ''' Returns tax object based on self.taxcode'''
       pass
  
   @property
   def tax_val_list(self):
      li=[]
      taxobj=self.get_tax_obj
      if self.amountsIncludeTax is False:
        if taxobj.taxcomp_exists is True:
          for item in taxobj.taxcomp_list:
            taxdict={ 'taxName':None, 'taxVal':None,'taxRate':None}
            taxdict['taxVal']=self.amt_aft_discount*item.rate
            taxdict['taxName']=item.name
            taxdict['taxRate']=item.rate
            li.append(taxdict)
      return li 
       
          
   def __str__(self):
      return self.description
    
  
    
class TaxCode:
   def __init__(self,tax,code):
      self.code=code
      self.name=tax.get('Name',None)
      self.components=tax.get('Components',None)
      self.taxRate=tax.get('TaxRate',None)
      self.taxRateType=tax.get('TaxRateType',None)
      self.rate=tax.get('Rate',None)
      self.account=tax.get('Account',None)
   
   @property  
   def taxcomp_list(self):
      taxcomp_list=[]
      for taxcomp in self.components:
        taxcomp_list.append(TaxCodeComponent(taxcomp))
      return taxcomp_list
   
   @property
   def taxcomp_exists(self):
   ''' Check if Tax Components exist, If inbuilt taxes are used they will contain a list with empty dicts 
   as below
   "Components": [
    {},
    {}
                 ]
   '''
      if self.rate is not None:
        return False
      else:
        return True
    
    
   def __str__(self):
      return self.name
  
class TaxCodeComponent:
   def __init__(self,taxcomp):
      self.name=taxcomp.get('Name',None)
      self.rate=taxcomp.get('Rate',None)
      self.account=taxcomp.get('Account',None)
    
   def __str__(self):
      return self.name
    

    
    
   
    
 
    
