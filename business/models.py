from django.db import models

# Create your models here.

class Business(models.Model):
  name=models.CharField("Business Name",max_length=50)
  code=models.CharField("Code",max_length=200)
  user=models.OneToOneField("auth.User")
  
  def __str__(self):
    return "%s" % self.name
  
  
