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

class SalesInvLine:
   def __init__(self,discount=0,amountsIncludeTax=None):
      self.amountsIncludeTax=amountsIncludeTax
      self.description=None
      self.account=None
      self.taxCode=None
      self.qty=None
      self.item=None
      self.amount=None
      self.discount=discount
      self.trackingCode=None
      self.customFields=None
      
      
      @property
      def amt_aft_discount(self):
        if self.discount is not None:
          return int(self.amount) -  ((int(self.amount)*int(self.discount))/100 )
        
        
    
   def __str__(self):
      return self.description
    

    
class TaxCode:
   def __init__(self):
      self.name=None
      self.components=None
      self.taxRate=None
      self.taxRateType=None
  
   def __str__(self):
      return self.name
  
class TaxCodeComponent:
   def __init__(self):
      self.name=None
      self.rate=None
      self.account=None
    
   def __str__(self):
      return self.name
    
   
    
 
    
