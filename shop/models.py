from django.db import models
import datetime
import os
 
# Create your models here.

def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  new_filename="%s %s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
 

 
class Product(models.Model):
  # category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  #vendor=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  #quantity=models.IntegerField(null=False,blank=False)
  #original_price=models.FloatField(null=True,blank=True)
  #selling_price=models.FloatField(null=True,blank=True)
  front_description=models.TextField(max_length=200,null=False,blank=False)
  description=models.TextField(max_length=5000,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  #trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name