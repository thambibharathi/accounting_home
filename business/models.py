from django.db import models

# Create your models here.

class Business(models.Model):
  name=models.CharField("Business Name",max_length=50)
  code=models.CharField("Code",max_length=200)
  user=models.ForeignKey("auth.User")
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return "%s" % self.name
 
class BusinessDetails(models.Model):
  BusinessName=models.CharField("Business Name",max_length=200,null=True,blank=True)
  BusinessContactInformation=models.CharField("Business Contact details", max_length=200,null=True,blank=True)
  BusinessIdentifier=models.CharField("Business Identifier",max_length=200,null=True,blank=True)
  
  
  
  
  
  
  
  
