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
  def __init__(self):
    self.name=None
    self.email=None
    self.telephone=None
    self.fax=None
    self.mobile=None
    self.notes=None
    self.address=None
    self.customFields=None
    self.code=None
    self.creditLimit=None
    
  def __str__(self):
    return self.name

class SalesInvoice:
   def __init__(self):
      self.issueDate=None
      self.reference=None
      self.to=None
      self.billingAddress=None
      self.lines=None
      self.dueDate=None
      self.discount=None
      self.amountsIncludeTax=None
      self.roundingMethod=None
      self.dueDateType=None
      self.dueDateDays=None
      self.latePaymentFees=None
      self.latePaymentFeesPercentage=None
      self.rounding=None
      
   def __str__(self):
      return self.reference

class SalesInvLine:
   def __init__(self):
      self.description=None
      self.account=None
      self.taxCode=None
      self.qty=None
      self.item=None
      self.amount=None
      self.discount=None
      self.trackingCode=None
      self.customFields=None
    
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
    
   
    
 
    
