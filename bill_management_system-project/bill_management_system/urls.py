"""static_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    #path('edithomepage/<int:size>', views.home,name='home2'),
    path('additemheader/', views.ItemHeaderCreateView.as_view(), name='add_itemheader'),
    path('itemheaderlist/', views.ItemHeaderList.as_view(), name='itemheader_list'),
    path('deleteitemheader/<int:pk>/', views.ItemHeaderDeleteView.as_view(), name='delete_itemheader'),
    path('updateitemheader/<int:pk>/', views.ItemHeaderUpdateView.as_view(), name='update_itemheader'),
    #path('additem/<str:itemheader_name>/', views.ItemCreateView.as_view(), name='add_item'),
    path('additem/<str:itemheader_name>/', views.ItemCreate, name='add_item'),
    #path('itemlist/', views.ItemList.as_view(), name='item_list'),
    path('itemlist/', views.itemlistview, name='item_list'),
    path('updateitem/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
    path('deleteitem/<int:pk>/', views.ItemDeleteView.as_view(), name='delete_item'),
    path('customerlist/', views.Customer_DetailListView.as_view(), name='customer_list'),
    path('bill/', views.bill, name='bill'),
    path('printbill/', views.print_bil, name='printbill'),
    path('billview/<int:c_id>', views.bill_view, name='bill_view'),
    path('deletecustomerdetail/<int:pk>/', views.Customer_DetailDeleteView.as_view(), name='delete_customer_detail'),
    path('searchbill/<int:bill_no>', views.search_bill, name='search_bill'),
    path('editpage/', views.edit_page, name='edit_page'),
    #path('showframe/',TemplateView.as_view(template_name='showframe.html'),name='showframe')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
