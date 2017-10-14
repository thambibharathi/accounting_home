class BusinessDetails:
  def __init__(self):
    self.tradingName=tradingName
    self.contactDetails=contactDetails
    self.businessIdentifier=businessIdentifier
    
  def __str__(self):
    return self.tradingName
    
class CustomerDetails:
  def __init__(self):
    self.name=None
    self.billingAddress=None
    self.email=None
    self.businessIdentifier=None
    self.code=None
    self.startingBalanceType=None
    self.telephone=None
    self.fax=None
    self.mobile=None
    self.notes=None
    self.customFields=dict()
    self.creditLimit=None
    self.startingBalanceType=None
    
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
    self.customFields=dict()
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
      
   def __str__(self):
      return self.reference

class SalesInvLine:
    def __init__(self):
      self.description=None
      self.account=None
      self.taxCode=None
      self.qty=None
      self.amount=None
      self.discount=None
      self.customFields=dict()
      
   def __str__(self):
      return self.description
      
      
    
