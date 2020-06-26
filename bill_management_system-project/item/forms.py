from django import forms
from . import models

class ItemHeaderForm(forms.Form):
    class Meta:
        model = models.ItemHeader
        fields = '__all__'
        
class ItemForm(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=100)
    item_price = forms.IntegerField(label='Item Price')