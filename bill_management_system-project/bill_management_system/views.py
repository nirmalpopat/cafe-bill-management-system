from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from item.forms import ItemHeaderForm,ItemForm
from item.models import Item,ItemHeader,CompleteBill,Customer_Detail
from django.urls import reverse_lazy
from item.utills import render_to_pdf
from django.http import HttpResponse
from django.core.files import File
from io import BytesIO
from django.http import FileResponse
#from twilio.rest import Client


customer_name = ''
customer_billno = ''
customer_mono = ''
customer_bill = ''
customer_bill_total = ''
item_div = ''
check_edit_page = 0

def home(request):
    global customer_bill,customer_billno,customer_mono,customer_name,customer_bill_total,item_div,check_edit_page
    if check_edit_page == 0:
        item_div = 3
    #item_div = 2
    c_name = ''
    c_mono = ''
    c_billno = ''
    if request.method == 'POST' and 'total_bill' in request.POST:
        
        bill_list = []
        
        c_name = request.POST['cname']
        c_mono = request.POST['cno']
        
        for i in Customer_Detail.objects.all():
            c_billno = i.id
        c_billno += 1
        customer_billno = c_billno
        customer_mono = c_mono
        customer_name = c_name
        
        for i in Item.objects.all(): 
            #print(i.item_name)
            item_price_detail = {}
            item_price_detail['item_header'] = i.itemheader
            item_price_detail['item_name'] = i.item_name
            item_price_detail['item_qty'] = request.POST[i.item_name]
            item_price_detail['item_price'] = i.item_price
            bill_list.append(item_price_detail)
            item_price_detail = {}
        
        print(bill_list,'      complete')

        bill_preview=[]
        item_total=[]
        for i in ItemHeader.objects.all():
            total=0
            for j in bill_list:
                if i.itemheader_name == j['item_header']:
                    
                    if j['item_qty'] != '':
                        d={}
                        d["item_header"]=j['item_header']
                        d["item_name"]=j['item_name']
                        d["item_qty"]=j['item_qty']
                        d["item_price"]=j["item_price"]
                        d["total"]=int(j["item_price"])*int(j['item_qty'])
                        
                        total=total+int(d["total"])
                        bill_preview.append(d)
                        d={}
            d={}
            d['item_name'] = i.itemheader_name
            d['item_total']=total
            item_total.append(d)
            d={}
        customer_bill = bill_preview
        print(bill_preview,'               bill_preview')
        print(item_total,'               item_total')
        total = 0
        for i in bill_preview:
            print(i['total'])
            total += int(i['total'])
        customer_bill_total = total
        
        #Add Value in Complete Bill of Customer
        
        
        
            
        
        
    else:
        item_total = []
        for i in ItemHeader.objects.all():
            d={}
            d['item_name'] = i.itemheader_name
            d['item_total']=''
            item_total.append(d)
            d={}
        bill_preview = []
        total = ''
        c_detail = Customer_Detail.objects.all()
        for i in c_detail:
            print(i.id,'               id')
            c_billno = i.id
        c_billno += 1
    if 'clear' in request.POST:
        item_total = []
        for i in ItemHeader.objects.all():
            d={}
            d['item_name'] = i.itemheader_name
            d['item_total']=''
            item_total.append(d)
            d={}
        bill_preview = []
        total = ''
        for i in Customer_Detail.objects.all():
            print(i.id,'               id')
            c_billno = i.id
        c_billno += 1
        
        #print(list(item_total))
    #print(sum(item_total['item_total']),'    total')   
    return render(request,'test.html',{'header':ItemHeader.objects.all,'item':Item.objects.all,'heder_form':ItemHeaderForm,'item_form':ItemForm,'val':item_div,'item_total':item_total,'bill_preview':bill_preview,'total':total,'c_name':c_name,'c_mono':c_mono,'c_billno':c_billno})

def bill(request):
    global customer_bill,customer_billno,customer_mono,customer_name,customer_bill_total
    print('Customer Details : ')
    print('No : ' , customer_billno)
    print('Mo No : ' , customer_mono)
    print('Name : ' , customer_name)
    print('Total : ' , customer_bill_total)
    print(customer_bill)
    #complete_bill = CompleteBill(bill_no=customer_billno,c_name=customer_name,c_mono=customer_mono)
    return render(request,'bill.html',{'bill_preview':customer_bill,'total':customer_bill_total,'c_name':customer_name,'c_mono':customer_mono,'c_billno':customer_billno})

def print_bil(request):
    global customer_bill,customer_billno,customer_mono,customer_name,customer_bill_total
    print(customer_name,'           bkjbkk')
    data = {'bill_preview':customer_bill,'total':customer_bill_total,'c_name':customer_name,'c_mono':customer_mono,'c_billno':customer_billno}
    pdf = render_to_pdf('bill.html',data)
    
    if customer_name != '' and customer_mono != '':
        print('heyyyyyyyyy')
        cust_detail = Customer_Detail()
        cust_detail.c_name = customer_name
        cust_detail.c_mono = customer_mono
        cust_detail.save()
        cust_detail_billpdf = Customer_Detail.objects.get(id=customer_billno)
        print(cust_detail_billpdf.c_name)
        pdf_name = str(customer_billno)
        cust_detail_billpdf.bill.save(pdf_name, File(BytesIO(pdf.content)))
        return HttpResponse(pdf, content_type='application/pdf')

class ItemHeaderCreateView(CreateView):
    form = ItemHeaderForm
    model = ItemHeader
    fields = '__all__'
    template_name = "add_itemheader.html"
    
class ItemHeaderList(ListView):
    model = ItemHeader
    context_object_name = 'itemheader_list'
    template_name='itemheader_list.html'
    

class ItemHeaderDeleteView(DeleteView):
    model = ItemHeader
    template_name='itemheader_confirm_delete.html'
    success_url = reverse_lazy("itemheader_list")
    

class ItemHeaderUpdateView(UpdateView):
    model = ItemHeader
    form = ItemHeaderForm
    fields = '__all__'
    template_name = "add_itemheader.html"
    

'''class ItemCreateView(CreateView):
    #form = ItemForm
    model = Item
    #fields = '__all__'
    fields = ['item_name','item_price']
    template_name = "item_form.html"
    
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        #context['itemheader'] = self.publisher
        #print(context['form']['itemheader'].name)
        #context['form']['itemheader'].value
        #print(context['form'])
        #How to Get data from url
        #context['form']['itemheader'].value = 'jk'
        #print(context['form']['itemheader'].value,'        value')
        print(self.kwargs['itemheader_name'])
        
        a = Item()
        a.itemheader = self.kwargs['itemheader_name']
        return context'''
    
def ItemCreate(request,itemheader_name):
    item_create_form = ItemForm
    print(item_create_form())
    if request.method == 'POST':
        items = Item()
        items.itemheader = itemheader_name
        items.item_name = request.POST['item_name']
        items.item_price = request.POST['item_price']
        items.save()
        return redirect('item_list')
    return render(request, 'item_form.html',{'form':item_create_form})

#Item Update

class ItemUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    template_name = "item_update.html"


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "item_confirm_delete.html"
    success_url = reverse_lazy("item_list")
    
class ItemList(ListView):
    model = Item
    context_object_name = 'Item'
    template_name='item_list.html'
    
def itemlistview(request):
    return render(request, 'itemlistview.html',{'header':ItemHeader.objects.all,'item':Item.objects.all})

#Customer List View

class Customer_DetailListView(ListView):
    model = Customer_Detail
    context_object_name = 'c_detail'
    template_name = "customer_detail_list.html"

def bill_view(request,c_id):
    #c_id -= 1
    print(c_id)
    file = open('D:/DEGREE/Django/DjangoProgram/bill_management_system-project/media/bill/'+str(c_id))
    try:
        return FileResponse(open("D:/DEGREE/Django/DjangoProgram/bill_management_system-project/media/bill/"+str(c_id),"rb"),content_type="application/pdf")
    except:
        return HttpResponse("<h1>gh</h1>")
    return FileResponse(open(file, 'rb'))

    '''with open('D:/DEGREE/Django/DjangoProgram/bill_management_system-project/media/bill/'+str(c_id)) as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed'''
    

class Customer_DetailDeleteView(DeleteView):
    model = Customer_Detail
    template_name = "customer_delete.html"
    #context_object_name = 'delete_detail'
    success_url = reverse_lazy("customer_list")

def search_bill(request,bill_no):
    print('heer')
    #file = open('D:/DEGREE/Django/DjangoProgram/bill_management_system-project/media/bill/'+str(bill_no))
    try:
        print('hi')
        return FileResponse(open("D:/DEGREE/Django/DjangoProgram/bill_management_system-project/media/bill/"+str(bill_no),"rb"),content_type="application/pdf")
    except:
        print('hiii')
        return HttpResponse("<h1>Inavailid ID</h1>")
    #return FileResponse(open(file, 'rb'))

#edit_page
def edit_page(request):
    global item_div,check_edit_page
    check_edit_page = 1
    if request.method == 'POST':
        item_div = request.POST['item_div_size'] 
        #return render(request, 'test.html')
        return redirect('home')
    return render(request, 'editpage.html')