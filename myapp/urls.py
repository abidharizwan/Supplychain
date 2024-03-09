"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("loginadmin/", views.loginadmin),
    path("loginpost/", views.loginpost),
    path("changepasswordadmin/", views.changepasswordadmin),
    path("changepasswordadminpost/", views.changepasswordadminpost),
    path("viewsupplieradmin/", views.viewsupplieradmin),
    path("viewsupplieradminpost/", views.viewsupplieradminpost),
    path("supplierapprove/<id>", views.supplierapprove),
    path("supplierreject/<id>", views.supplierreject),
    path("approvesupplieradmin/", views.approvesupplieradmin),
    path("rejectsupplieradmin/", views.rejectsupplieradmin),
    path("viewmanufactureadmin/", views.viewmanufactureadmin),
    path("viewmanufactureadminpost/", views.viewmanufactureadminpost),
    path("manufactureapprove/<id>", views.manufactureapprove),
    path("manufacturereject/<id>", views.manufacturereject),
    path("approvemanufactureadmin/", views.approvemanufactureadmin),
    path("rejectmanufactureadmin/", views.rejectmanufactureadmin),
    path("viewselleradmin/", views.viewselleradmin),
    path("viewselleradminpost/", views.viewselleradminpost),
    path("sellersapprove/<id>", views.sellersapprove),
    path("sellersreject/<id>", views.sellersreject),
    path("approveselleradmin/", views.approveselleradmin),
    path("rejectselleradmin/", views.rejectselleradmin),
    path("viewcomplaintadmin/", views.viewcomplaintadmin),
    path("viewcomplaintadminpost/" , views.viewcomplaintadminpost),
    path("sendreply/<id>", views.sendreply),
    path("sendreplypost/", views.sendreplypost),
    path("viewfeedback/", views.viewfeedback),
    path("viewfeedbackpost/" , views.viewfeedbackpost),
    path("viewuser/", views.viewuser),
    path("viewuserpost/" ,views.viewuserpost),
    path("adminhome/", views.adminhome),



    path("signupsupplier/", views.signupsupplier),
    path("signupsupplierpost/" , views.signupsupplierpost),
    path("loginsupplier/", views.loginsupplier),
    path("viewprofilesupplier/", views.viewprofilesupplier),
    path("editsupplier/", views.editsupplier),
    path("editsupplierpost/", views.editsupplierpost),
    path("addrawmaterialssupplier/", views.addrawmaterialssupplier),
    path("managerawmaterialsaddsupplierpost/", views.managerawmaterialsaddsupplierpost),
    path("viewrawmaterialsedit/", views.viewrawmaterialsedit),
    path("viewrawmaterialspost/", views.viewrawmaterialspost),
    path("editrawmaterials/<id>", views.editrawmaterials),
    path("editrawmaterialspost/", views.editrawmaterialspost),
    path("deleterawmaterials/<id>", views.deleterawmaterials),
    path("viewstock/", views.viewstock),
    path("addstocksupplier/", views.addstocksupplier),
    path("addstocksupplierpost/", views.addstocksupplierpost),
    path("editstocksupplier/<id>", views.editstocksupplier),
    path("editstocksupplierpost/", views.editstocksupplierpost),
    path("deletestocksupplier/<id>", views.deletestocksupplier),
    path("viewordersfrommanufacture/", views.viewordersfrommanufacture),
    path("viewordersub/<id>", views.viewordersub),
    path("updateorderstatussupplier/<id>", views.updateorderstatussupplier),
    path("supplierhome/", views.supplierhome),

    path("signupmanufacture/", views.signupmanufacture),
    path("signupmanufacturepost/", views.signupmanufacturepost),
    # path("loginmanufacture/", views.loginmanufacture),
    path("changepasswordmanufacture/", views.changepasswordmanufacture),
    path("changepasswordmanufacturepost/" , views.changepasswordmanufacturepost),
    path("viewprofilemanufacture/", views.viewprofilemanufacture),
    path("manufactureeditprofile/ ", views.manufactureeditprofile),
    path("manufactureeditpost/", views.manufactureeditpost),
    path("viewsupplier/", views.viewsupplier),
    path("viewrawmaterialsandsendorder/", views.viewrawmaterialsandsendorder),
    path("viewmanufactureproduct/", views.viewmanufactureproduct),
    path("viewmanufactureproductpost/", views.viewmanufactureproductpost),
    path("managemanufactureproductadd/", views.managemanufactureproductadd),
    path("managemanufactureproductaddpost/",views.managemanufactureproductaddpost),
    path("managemanufactureproductedit/", views.managemanufactureproductedit),
    path("manufactureproductdelete/<id>", views.manufactureproductdelete),
    path("managemanufactureproducteditpost/", views.managemanufactureproducteditpost),
    path("viewsellerorderandverify/", views.viewsellerorderandverify),
    path("viewsellerorderandverifypost/", views.viewsellerorderandverifypost),
    path("manufacturehome/", views.manufacturehome),

    path("signupseller/", views.signupseller),
    path("signupsellerpost/", views.signupsellerpost),
    path("loginseller/", views.loginseller),
    path("viewandeditprofile/", views.viewandeditprofile),
    path("viewcustomerorder/", views.viewcustomerorder),
    path("viewcustomerorderpost/", views.viewcustomerorderpost),
    path("viewpayments/", views.viewpayments),
    path("viewpaymentspost/", views.viewpaymentspost),
    path("updateorderstatus/", views.updateorderstatus),
    path("viewmanufacture/", views.viewmanufacture),
    path("viewmanufacturepost/", views.viewmanufacturepost),
    path("viewmanufacturingproducts/", views.viewmanufacturingproducts),
    path("viewmanufacturingproductspost/", views.viewmanufacturingproductspost),
    path("viewpurchase/", views.viewpurchase),
    path("viewpurchasepost/", views.viewpurchasepost),
    path("addproductstosale/", views.addproductstosale),
    path("sellerhome/", views.sellerhome),

]
