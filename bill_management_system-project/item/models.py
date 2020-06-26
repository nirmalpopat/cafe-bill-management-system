from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class ItemHeader(models.Model):
    itemheader_name = models.CharField(unique=True,max_length=50)
    
    def get_absolute_url(self):
        return reverse("itemheader_list")
    
    def __str__(self):
        return self.itemheader_name
    
    
class Item(models.Model):
    itemheader =models.CharField(max_length=50)
    item_name = models.CharField(unique=True,max_length=50)
    item_price = models.IntegerField()
    
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("item_list")
    
class Customer_Detail(models.Model):
    c_name =models.CharField(max_length=50)
    c_mono = models.CharField(max_length=50)
    bill = models.FileField(upload_to="bill/",blank=True)
    
    def __str__(self):
        return self.c_name
    
class CompleteBill(models.Model):
    bill_no = models.IntegerField(default=0)
    c_name =models.CharField(max_length=50)
    c_mono = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    item_qty = models.IntegerField()
    item_price = models.IntegerField()
    item_total = models.IntegerField()
    bill_date = models.DateField(default=timezone.now)
    #bill_detail = models.ForeignKey(SubBill, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.c_name